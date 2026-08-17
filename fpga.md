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
