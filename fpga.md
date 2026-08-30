# FPGA - SLG47910V - Shrike Lite

## Important

- Renesas **GreenPAK** family, breaks this rule by baking analog components right next to the logic gates.
- SLG47910V is a purely digital low-power FPGA from **ForgeFPGA** family

### CLB

What it is: CLB stands for Configurable Logic Block. In Renesas/ForgeFPGA terminology, these are sometimes called RBBs (Routing Basic Blocks). Think of these as the physical "neighborhoods" or "tiles" on the silicon chip. Each block contains a cluster of logic gates and memory flip-flops.

### LUT

What it is: LUT stands for Look-Up Table. This is the fundamental brain of the FPGA. Instead of fixed AND/OR gates, an FPGA uses LUTs to calculate any Boolean logic equation you write in Verilog.

### FF

What it is: FF stands for Flip-Flop. These are the tiny memory registers that hold a single bit (1 or 0) between clock cycles. Every time you write reg [7:0] my_var; in your Verilog, you are using 8 Flip-Flops.

### BRAM

What it is: BRAM stands for Block RAM. While Flip-Flops are good for storing small, fast variables, BRAMs are large chunks of dedicated SRAM memory (like the cache in a CPU) used for storing large arrays, buffers, or lookup tables. The SLG47910V has 8 of these blocks, each holding 4 kilobits of data.

### IP 

Intellectual Property core — a packaged, reusable hardware block with a defined interface

### DSP48E2

What it is: A dedicated, hardened DSP slice found on Xilinx UltraScale/UltraScale+ FPGAs (the "E2" marks that generation; earlier devices used DSP48E1). Each slice packs a 27×18 multiplier, a 48-bit adder/accumulator, and a pattern detector into one fixed silicon block, purpose-built for multiply-accumulate math (filters, FFTs, counters, checksums). Using DSP48E2s instead of building the same arithmetic from LUTs/FFs is faster and far cheaper on fabric resources. A utilization report line like "52 DSP48E2" means the design's arithmetic was mapped onto 52 of these hard blocks. This is a Xilinx-specific hard IP — it has no equivalent on the ForgeFPGA SLG47910V, whose arithmetic (e.g., carry chains, see below) is built from general LUT/FF fabric instead.

* **27×18 multiplier:** the two operand widths the hard multiplier accepts — one input up to 27 bits, the other up to 18 bits — producing up to a 45-bit product in a single clock. Multiply anything wider and the tool must cascade multiple DSP48E2 slices or spill part of the math onto LUTs/FFs.
* **Pattern detector:** a built-in comparator that checks the ALU/adder output against a target bit pattern (with an optional mask) and raises a flag on match — used for things like counter terminal-count detection, overflow/saturation flags, and convergent rounding, all without spending extra LUTs on a separate comparator.

#### Common DSP48E2 Use Cases

| Operation | What it needs | How DSP48E2 helps |
|---|---|---|
| FIR filter | Multiply + accumulate, repeated | One DSP48E2 per tap (multiply + add every clock) |
| IIR filter | Multiply + accumulate with feedback | Same, but output feeds back into the next input |
| FFT (twiddle multiply) | Complex multiply per butterfly stage | 3–4 DSP48E2s per butterfly |
| Correlation / matched filter | Same math as FIR, different data | Same tap structure |
| Matrix multiplication | Repeated multiply-accumulate (dot products) | Systolic array of DSP48E2s |
| CIC decimation/interpolation | Mostly adders, few/no multiplies | Uses the adder half of the slice |

**FIR filter example:** a FIR filter computes `y[n] = h[0]*x[n] + h[1]*x[n-1] + ... + h[N-1]*x[n-N+1]`. Each term is one multiply, and summing them is one accumulate — exactly what a single DSP48E2 does per clock. A 16-tap FIR maps onto roughly 16 DSP48E2 slices running in parallel, so the whole filter output is ready every clock cycle instead of looping like a CPU would.

**FFT butterfly example:** an FFT is built from repeated "butterfly" steps, each multiplying a data sample by a complex "twiddle factor": `(a + jb) * (c + jd) = (ac - bd) + j(ad + bc)`. Done directly that's 4 real multiplies + 2 adds. FPGA FFT cores instead use a 3-multiply trick: `m1 = c*(a+b)`, `m2 = a*(d-c)`, `m3 = b*(c+d)`, giving `real = m1 - m3` and `imag = m1 + m2` — 3 DSP48E2 multiplies instead of 4 per butterfly, using the slices' built-in adders for the surrounding sums.

#### Practical Example: Microphone → FFT → Spectrum Analyzer

A common real-world pipeline built on this hardware:

1. A microphone's analog signal is sampled by an ADC — e.g., 48 kHz, 16-bit PCM — and streamed into the PL as a continuous sample stream (often over AXI-Stream).
2. Samples are buffered (in BRAM or a FIFO) until a full frame is collected — e.g., 1024 samples.
3. That frame is fed into a streaming FFT IP core (e.g., a 1024-point FFT, which is log2(1024) = 10 butterfly stages). Every butterfly's complex multiply runs on DSP48E2 slices as described above.
4. The FFT output is 1024 complex frequency bins; taking the magnitude of each bin (`sqrt(re² + im²)`, often approximated via CORDIC to avoid a square root) produces the audio spectrum — which bins are loud, which are quiet.
5. That spectrum feeds whatever's next: an equalizer, a voice-activity detector, a keyword-spotting front end, etc.

Because the DSP48E2 slices run the multiply-accumulate math in parallel, a 1024-point FFT frame (which arrives once every ~21 ms at 48 kHz) computes in a handful of clock cycles — comfortably real-time with huge margin to spare. The same pipeline shape applies to a camera sensor, just in 2D: image rows/columns run through row-wise then column-wise FFTs (or a related transform like the DCT used in JPEG) for frequency-domain filtering or compression, again with each 1D transform's butterflies mapped onto DSP48E2s.

### RTL

What it is: RTL stands for Register Transfer Level. It's the abstraction level used to describe digital logic in terms of how data moves between registers (Flip-Flops) each clock cycle, and the combinational logic (LUTs) that computes it along the way. Verilog and VHDL are RTL description languages — writing `sum <= num1 + num2;` is describing an RTL transfer. This is the "logical design" referred to elsewhere in this doc (the `.v` file); synthesis converts RTL into the actual LUTs/FFs/routing on the chip.

### Vivado

What it is: Vivado Design Suite is AMD/Xilinx's FPGA design tool. It covers synthesis, Place and Route (PnR), timing analysis, and bitstream generation for Xilinx FPGAs. It plays the same role for Xilinx devices that ForgeFPGA Designer's synthesis engine + I/O Planner + PnR flow (described below) plays for the SLG47910V — but Vivado does **not** target ForgeFPGA/GreenPAK devices, which use their own toolchain (e.g., Renesas Go Configure / ForgeFPGA Designer).

### Vitis

What it is: Vitis is AMD/Xilinx's unified software development platform, built on top of Vivado. Vivado handles the hardware side (RTL → synthesis → bitstream); Vitis handles the software/embedded side — compiling C/C++ applications that run on an embedded processor (e.g., the Arm cores in a Zynq SoC), and building HLS (High-Level Synthesis) kernels that get compiled from C/C++ into hardware accelerators for the FPGA fabric.

### PS (Processing System)

What it is: On a Xilinx **Zynq** / Zynq UltraScale+ SoC, the PS is the hard-wired processor side of the chip — one or more Arm Cortex cores (e.g., Cortex-A9, Cortex-A53, Cortex-R5) plus fixed peripherals (DDR memory controller, UART, USB, Ethernet, GPIO). It's a regular embedded CPU subsystem, not reconfigurable — it runs Linux, a bare-metal app, or an RTOS, and is programmed in C/C++ via **Vitis**.

### PL (Programmable Logic)

What it is: The FPGA fabric side of a Zynq SoC — the reconfigurable LUTs, FFs, CLBs, and BRAM described throughout this document. Programmed with RTL (Verilog/VHDL) and synthesized/routed via **Vivado**, and can be reprogrammed (new bitstream loaded) at runtime independently of the PS.

**PS ↔ PL relationship:** they sit on the same die and talk over on-chip AXI interconnects. A typical flow: the PS boots (Linux or bare-metal), loads a bitstream into the PL, then drives/reads custom PL logic through memory-mapped AXI registers or DMA. This split — fixed processor (PS) + reconfigurable fabric (PL) — is specific to Xilinx's Zynq family; the standalone SLG47910V covered elsewhere in this doc is PL-only, with no on-chip hard processor.

---
## Math

The Math on the Chip Specification - SLG47910V

```text
140 CLBs (RBBs)
1120 LUTs
1120 FFs
```

If you divide those numbers, you can see exactly how the chip is physically built!
**1120 / 140 = 8**.

This means every single one of the **140 CLBs** on the  chip contains exactly **8 LUTs** and **8 Flip-Flops**.

---

## Place and Route (PnR)

### Floor Plan / Floorplan (ForgeFPGA Designer)

"Floor plan" has two related meanings in the ForgeFPGA tool, both part of the PnR stage:

1. **Floor planning (an automated PnR sub-step):** ForgeFPGA Designer's build flow runs *technology mapping → clustering and floor planning → placement and optimization → routing → resource calculation*. Floor planning here is the step where the synthesized netlist's LUTs/FFs are clustered and assigned into CLBs/RBBs (see [CLB](#clb) above) and given a rough region on the die, before final placement fine-tunes exact locations and routing wires them together. It's fully automatic — unlike the I/O Planner, there's no manual pin-assignment step for it.
2. **The Floorplan window (a GUI view):** a visualization inside the FPGA Editor that shows the *result* of that PnR run — the physical placement of each CLB/RBB and FF on the die grid, resource utilization (shown in the top-left corner), and how the netlist's primitives are placed and interconnected, including how I/O ports map to internal blocks and GPIOs. Open it via the **Floorplan** button on the toolbar or **Windows → Floorplan** in the main menu; the bottom toolbar navigates/zooms the die view, and clicking a component shows its details in a block configuration info panel.

In short: the I/O Planner (above) controls *where ports connect to pins*; the Floorplan tells you *where the synthesized logic actually landed on the die* after PnR — useful for the same kind of diagnosis as the [CLB saturation / logic fragmentation](#resource-utilization-clb-saturation-vs-unused-luts) discussion below, since seeing clustered-but-sparse CLBs in the Floorplan view is often the visual symptom of that.

## .ffpga (ForgeFPGA Design File)

## .v (Verilog Source File)

## low-power ForgeFPGA™ family (like the SLG47910V)

### The Relationship: Logic Meets Physics

* **The `.v` File (Logical Design):**  top-level Verilog file defines the abstract logic and the input/output ports of  design. For example, you might declare `input sys_clk` and `output sensor_data` without knowing where those signals physically exist on the chip.
* **The I/O Planner (Physical Mapping):** The I/O Planner is a configuration tool that maps the logical ports defined in  `.v` file to the physical pins and hard IP blocks on the actual FPGA die.

When you open the I/O Planner, it reads the port declarations directly from  synthesized `.v` code. You then assign those ports to physical resources, such as:

* **GPIOs:** Routing  inputs and outputs to specific external pad coordinates.
* **Dedicated Hard IP:** Connecting  Verilog signals to built-in silicon features, like routing a clock net to an internal oscillator or configuring a pin for specific VDDIO voltage levels (e.g., 1.8V vs 3.3V).

1. **Write the Verilog:** Defines ports.
You write the `.v` code defining the top-level module. The compiler identifies all `input`, `output`, and `inout` port names.


2. **Synthesize the Logic:**
The ForgeFPGA synthesis engine compiles the Verilog into a netlist, turning  code into abstract logic gates and flip-flops.


3. **Map in the I/O Planner:** Assigns physical coordinates.
You open the I/O Planner table. By double-clicking a physical pin's "PORT" column, you select the matching port name from a drop-down list of all the ports defined in  `.v` file.


4. **Generate the Bitstream:**
During the Place and Route (PnR) phase, the compiler uses the I/O Planner's mapping file to physically wire the internal logic fabric out to the correct physical pads on the chip, generating the final bitstream.

For a device like the SLG47910, this mapping step is critical because you must explicitly connect  logic to its internal 50 MHz oscillator, PLLs, or distributed memory blocks rather than just assigning external I/O pins.

---

## Architecture Reference: LUTs, FFs, and CLBs

### 1. Overview

In Field-Programmable Gate Array (FPGA) architecture, Look-Up Tables (LUTs), Flip-Flops (FFs), and Configurable Logic Blocks (CLBs) are fundamentally distinct hardware components. However, they are physically integrated into a strict hierarchical structure. LUTs and FFs serve as the base operational units, while CLBs act as the physical containers that group them together.

### 2. Base Components

#### Look-Up Tables (LUTs)

* **Function:** The primary computational unit of the FPGA.
* **Behavior:** Purely combinational. A LUT acts as a programmable truth table capable of implementing any Boolean logic equation (e.g., AND, OR, XOR, addition).
* **Timing:** Data evaluates continuously; there is no clock dependency or memory state.

#### Flip-Flops (FFs)

* **Function:** The primary storage unit of the FPGA.
* **Behavior:** Purely sequential memory. A flip-flop (typically a D-type register) captures and holds a single bit of data (`1` or `0`).
* **Timing:** State changes occur strictly on designated clock edges (e.g., the positive edge of a 50 MHz clock).

### 3. Structural Hierarchy: The CLB / RBB

To optimize physical wiring and signal routing across the silicon, FPGA manufacturers do not scatter LUTs and FFs arbitrarily. They are packaged together into repeating, standardized tiles known as **Configurable Logic Blocks (CLBs)**, or in some architectures (such as Renesas ForgeFPGA), **Routing Basic Blocks (RBBs)**.

A single CLB/RBB is a physical silicon boundary that contains:

1. A fixed number of LUTs.
2. A fixed number of FFs.
3. Internal multiplexers (routing switches) to connect them.

#### Case Study: SLG47910V Architecture

The physical ratio of components within a CLB can be derived directly from device specifications or synthesis resource reports. For the SLG47910V:

* Total Device CLBs (RBBs): 140
* Total Device LUTs: 1120
* Total Device FFs: 1120

Calculating the ratio ($1120 \div 140 = 8$) reveals the internal architecture of the chip. Every individual CLB physically contains exactly **8 LUTs and 8 Flip-Flops**.

### 4. Hardware Interaction and Data Flow

The physical proximity of LUTs and FFs within a single CLB is optimized for the most common digital logic pattern: calculating a value and immediately storing it on the next clock cycle (e.g., `sum <= num1 + num2;`).

**Standard Signal Path:**

1. **Logic Phase:** Input signals enter the CLB and are processed by the **LUT**.
2. **Internal Routing:** The combinational output from the LUT travels across a microscopic, dedicated internal wire directly to the input pin of an adjacent **FF** located within the same CLB.
3. **Storage Phase:** Upon the next clock tick, the **FF** captures the computed value.

When a digital design requires more logical operations than a single CLB can provide (greater than 8 LUTs in the case of the SLG47910V), the synthesis tool routes the signal out of the current CLB, across the FPGA's general routing matrix, and into an adjacent CLB to continue processing. High logic utilization across a design forces the routing tool to utilize a higher percentage of the available CLBs on the physical die.

---
## Resource Utilization: CLB Saturation vs. Unused LUTs

### 1. Overview

In FPGA synthesis, it is common to encounter a Resource Utilization Report where Configurable Logic Block (CLB) usage reaches 100%, even while a significant percentage of Look-Up Tables (LUTs) and Flip-Flops (FFs) remain unused. This phenomenon is known as **logic fragmentation** or **underpacking**.

Although a single CLB contains multiple LUTs and FFs (e.g., 8 LUTs and 8 FFs), the synthesis tool is rarely able to pack them to 100% capacity due to physical architectural constraints.

### 2. Root Causes of Logic Fragmentation

#### Input/Output Pin Congestion (Routing Limitations)

* **Mechanism:** While a CLB may contain 8 LUTs, the CLB itself has a strict, limited number of physical input and output wires connecting it to the rest of the chip.
* **Result:** If a design places 3 complex LUTs inside a CLB that require many unique input signals, those 3 LUTs may consume all available routing tracks leading into that specific CLB. The remaining 5 LUTs are left physically inaccessible. The synthesis tool must open a new CLB to place the next piece of logic, leaving the unused LUTs permanently trapped.

#### Control Set Conflicts

* **Mechanism:** A "Control Set" consists of the Clock, Reset, and Clock Enable signals. To save wiring, all the Flip-Flops inside a single CLB typically share the same Control Set.
* **Result:** If a design utilizes multiple different reset signals or clock enables, the associated Flip-Flops cannot physically coexist in the same CLB. The synthesis tool is forced to distribute these Flip-Flops across multiple CLBs, artificially inflating CLB usage while leaving adjacent LUTs and FFs empty.

#### Carry Chain and Arithmetic Constraints

* **Mechanism:** Dedicated arithmetic logic (like addition or counters) relies on high-speed "carry chains." These chains are hardwired vertically between specific CLBs to ensure fast mathematical operations.
* **Result:** The synthesis tool must place mathematical logic in strict alignments to utilize these physical carry chains. This rigid placement often prevents the tool from packing unrelated general logic into the remaining empty LUTs within those specific CLBs.

#### Timing Optimization and "Spreading"

* **Mechanism:** If a design does not strictly require the entire chip's capacity, synthesis tools are programmed to prioritize timing performance over area efficiency.
* **Result:** The tool will intentionally spread logic out across all available CLBs. Packing LUTs too densely can create localized routing congestion, which delays signal propagation and degrades the maximum clock frequency. By distributing the logic, the tool lowers CLB density, shortens wire lengths, and improves timing closure.

---

## Simulation Options

Before spending time on synthesis and Place and Route, RTL is verified in simulation: the `.v` design is run against a testbench (either another Verilog file, or a C++/Python harness) to check functional correctness. Simulators differ mainly in speed, language support, and whether they model gate/timing delays or just behavior.

### Verilator

What it is: A free, open-source Verilog/SystemVerilog simulator that **compiles** RTL into C++ (or SystemC) rather than interpreting it, making it one of the fastest simulators available. It's behavioral-only (no gate delays), and requires a C++ testbench that instantiates the compiled model — there's no built-in `$display`-driven native testbench flow like a traditional simulator. Common choice for CI regression suites and cycle-accurate co-simulation with a CPU/software model.

### Icarus Verilog (iverilog)

What it is: A free, open-source Verilog simulator/compiler. It **interprets** compiled RTL rather than converting it to C++, so it's generally slower than Verilator, but it's simpler to set up and runs traditional Verilog testbenches directly (`$display`, `$dumpfile`/`$dumpvars` for waveforms) without writing any C++.

### Vivado Simulator (XSIM)

What it is: The simulator bundled with AMD/Xilinx Vivado. Integrated GUI and waveform viewer, convenient when a design already targets Vivado since no separate toolchain install is needed. Not applicable to ForgeFPGA designs (see [Vivado](#vivado) above).

### ModelSim / QuestaSim

What it is: Commercial simulators from Siemens EDA. Industry-standard for mixed-language (Verilog + VHDL) simulation, widely used for larger/professional ASIC and FPGA verification flows.

### GHDL

What it is: A free, open-source VHDL simulator — effectively the VHDL-world equivalent of Icarus Verilog.

### Quick comparison

| Simulator | License | Speed | Notes |
|---|---|---|---|
| Verilator | Open-source | Fastest (compiles to C++) | Needs a C++/SystemC testbench; behavioral only |
| Icarus Verilog | Open-source | Moderate (interpreted) | Native Verilog testbenches, easy setup |
| Vivado Simulator (XSIM) | Free with Vivado | Moderate | Best when already inside the Vivado flow |
| ModelSim / QuestaSim | Commercial | Moderate–fast | Mixed Verilog + VHDL, industry standard |
| GHDL | Open-source | Moderate | VHDL only |

---

## Digital Logic Fundamentals (the actual hard part)

Tool flows (Vivado, ForgeFPGA Designer, simulators) are mechanical to pick up. The actual skill is digital logic — the concepts below are what separate "I can write Verilog that compiles" from "I can write Verilog that works and closes timing."

### Combinational vs. Sequential Logic

* **Combinational logic:** output depends only on the *current* inputs, with no memory of the past. Pure LUT logic — `assign y = a & b;`. No clock involved; output changes the instant an input changes (after gate delay).
* **Sequential logic:** output depends on current inputs *and* stored state from previous clock cycles. Built from FFs (see below) plus the combinational logic feeding them — `always @(posedge clk) sum <= a + b;`.

Every real design is a mix: combinational logic computes a next value, and sequential logic (FFs) captures it on the clock edge so it's stable and available for the next stage.

### Clocks, Edges, and Flip-Flops vs. Latches

* **Clock edge:** the instant a clock signal transitions — rising edge (`posedge`, 0→1) or falling edge (`negedge`, 1→0). Nearly all synchronous designs use `posedge` only; mixing both edges of the same clock in one design is a common source of timing headaches.
* **Flip-flop (FF):** edge-triggered storage. It samples its input at the clock edge and holds that value until the *next* edge — `always @(posedge clk) q <= d;`. This is the standard, safe building block for sequential logic.
* **Latch:** level-triggered storage. It's transparent (output follows input) whenever an enable signal is high, and holds its value when the enable is low — `always @(*) if (en) q = d;`. Latches are usually *unintentional* in FPGA design: an `always @(*)` block with an incomplete `if`/`case` (missing `else`, missing default) infers a latch because synthesis has to remember the last value for the unhandled condition. Synthesis tools flag this ("latch inferred") and it's almost always a bug, not a choice — FPGA fabric has dedicated FF resources but no equivalent dedicated latch resource, so an inferred latch burns LUTs to emulate one and behaves worse under timing analysis.

Rule of thumb: sequential logic in FPGA Verilog should be `always @(posedge clk)` blocks using non-blocking assignment (`<=`); combinational logic should be `always @(*)` blocks with every branch assigning every output, using blocking assignment (`=`).

### Finite State Machines (FSMs)

An FSM is sequential logic organized around a small set of named states (an FF-backed state register) plus combinational logic that computes the next state and outputs from the current state and inputs. This is the pattern underneath nearly every non-trivial core — IDLE → LOAD → COMPUTE → DONE style control logic — including cores like `mlp_ip.v` and `mlkem_ntt_ip.v`, where an FSM sequences multiply-accumulate or NTT butterfly operations across multiple clock cycles instead of trying to do the whole computation combinationally in one cycle.

Standard structure (two always blocks):

```verilog
// State register (sequential)
always @(posedge clk or posedge rst)
    if (rst) state <= IDLE;
    else     state <= next_state;

// Next-state + output logic (combinational)
always @(*) begin
    next_state = state;          // default: hold
    case (state)
        IDLE:    if (start) next_state = LOAD;
        LOAD:    next_state = COMPUTE;
        COMPUTE: if (done_flag) next_state = DONE;
        DONE:    next_state = IDLE;
    endcase
end
```

Splitting state storage (clocked) from next-state computation (combinational) keeps the FSM synthesizable, avoids accidental latches, and makes the state transitions easy to read directly out of the combinational block.

### Timing: Setup/Hold Time, Clock Domains, Metastability

This is the category that doesn't show up as a functional bug in simulation — the logic behaves correctly in simulation, but the physical chip can still fail, which is exactly what showed up as the ML-KEM timing closure issue.

* **Setup time:** the minimum time a data input must be stable *before* the clock edge for the FF to reliably capture it. Violated when the combinational logic feeding an FF takes too long to settle relative to the clock period — the classic "too much logic between two FFs for this clock frequency" problem. Fixed by reducing logic depth (pipelining — adding an FF stage to break up the combinational path) or lowering clock frequency.
* **Hold time:** the minimum time a data input must remain stable *after* the clock edge. Violated when a signal changes too quickly after the edge, usually from a path with too *little* delay (e.g., a signal racing through almost no logic to a downstream FF). Unlike setup violations, hold violations can't be fixed by slowing the clock — they need routing/delay fixes, which is why they're normally caught and fixed by the P&R tool itself.
* **Clock domain:** a region of logic driven by one clock signal. A design with more than one clock (e.g., a slow control clock and a fast DSP clock) has multiple clock domains. **Clock Domain Crossing (CDC):** any signal that passes from one clock domain to another is not sampled at a defined, predictable time relative to the destination clock — setup/hold guarantees only hold within a single domain.
* **Metastability:** what happens when a FF's setup/hold window is violated — its output can go to an invalid, undefined voltage level for an unbounded time before resolving to a 0 or 1, and it can resolve to the *wrong* value or propagate downstream before settling. This is the mechanism that makes CDC dangerous: a signal crossing domains isn't guaranteed to line up with setup/hold on the receiving side, so without protection it can occasionally send a receiving FF metastable. Standard mitigation is a **two-FF (or three-FF) synchronizer** on the receiving domain — it doesn't prevent metastability, it just gives a metastable FF's output extra clock cycles to resolve before anything downstream depends on it. Multi-bit buses crossing domains need more than a synchronizer (e.g., a gray-coded pointer or a proper async FIFO), since independent per-bit synchronizers can let different bits resolve on different cycles and hand downstream logic a bus value that was never valid at any instant.

Timing closure, concretely, is the P&R tool checking every FF-to-FF path in the design against setup/hold requirements at the target clock frequency and reporting slack (positive = margin, negative = violation, and negative slack is a real, physical failure mode — not a simulation artifact).

### Verilog vs. VHDL

Both are RTL description languages (see [RTL](#rtl) above) for the same underlying hardware concepts — the choice is tooling/ecosystem, not capability. Verilog is more common in industry outside aerospace/defense (which skews VHDL, partly for historical DoD-mandate reasons); it has C-like syntax and is generally considered faster to write and read. VHDL is strongly typed and more verbose, which some teams prefer for catching mistakes at compile time. This doc and the SLG47910V flow use Verilog.

### The Critical Mental Shift: HDL Describes Parallel Hardware, Not Sequential Code

This is the single biggest trap for anyone coming from software. An HDL module doesn't execute top-to-bottom like a program — every `always` block, every `assign` statement, in the entire module runs **simultaneously and continuously**, all the time, forever (modeling physical wires and gates that are all live at once). There's no "line 1 finishes, then line 2 starts."

```verilog
always @(posedge clk) a <= b;
always @(posedge clk) c <= a;
```

A software mind reads this as "a becomes b, then c becomes the new a" — i.e., c ends up equal to b on the same edge. That's wrong. Both blocks fire on the *same* clock edge, and both read the *old* (pre-edge) value of their right-hand side, because non-blocking assignment (`<=`) schedules the update rather than performing it immediately. So `c` gets the *old* `a` (from before this edge), not `b`. This is real hardware behavior: `a` and `c` are separate physical FFs, both driven by the same clock, both sampling their inputs at the same instant — `c`'s FF has no way to see a value `a`'s FF hasn't finished capturing yet. Getting this wrong is what produces one-cycle-off bugs that simulate "almost right" and are genuinely confusing until the parallel-hardware model clicks.

The practical rules that fall out of this: use `<=` (non-blocking) for anything inside a clocked (`always @(posedge clk)`) block, and `=` (blocking) inside purely combinational (`always @(*)`) blocks — mixing them within the same block is a common source of subtle simulation-vs-synthesis mismatches. And when reading a module, don't ask "what happens next" — ask "what is every block doing, at once, on this clock edge."
