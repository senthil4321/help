# FPGA - SLG47910V - Shrike Lite

## Important

- Renesas **GreenPAK** family, breaks this rule by baking analog components right next to the logic gates.
- SLG47910V is a purely digital low-power FPGA from **ForgeFPGA** family

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

