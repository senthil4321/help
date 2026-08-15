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

