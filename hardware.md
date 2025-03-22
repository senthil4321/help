# Information about hardware development

## Ref.

1. https://www.brusa.biz/fileadmin/template/Support-Center/ZD_007_Sample_definition_Project_management_EN.pdf

## Sample
1. A
1. B
1. C
1. D
### vesc
* http://vedder.se/2012/12/debugging-the-stm32f4-using-openocd-gdb-and-eclipse/
### pcb
pcbite
grit stone 2 um
diomond lapping stone
3 axis micrometer

### gdb, openocd and swd/jtag

#### GDB

The frontend where the developer interacts with debugging commands (e.g., break, step, run).
Communicates with OpenOCD over a TCP/IP connection.

#### OpenOCD:

Acts as the middleware that translates GDB commands into low-level operations.
Sends these operations to the target device via SWD or JTAG.

#### SWD/JTAG:

The physical interface that connects OpenOCD to the target microcontroller.
Allows OpenOCD to control the microcontroller, halt execution, and access memory/registers.
Target Device:

The microcontroller being debugged (e.g., ARM Cortex-M PICO).
Executes the program and responds to debugging commands.

```
+-------------------+       TCP/IP       +-------------------+       SWD/JTAG       +-------------------+
|                   | <----------------> |                   | <-----------------> |                    |
|       GDB         |       Commands     |     OpenOCD       |   Low-Level Ops     |   Target Device    |
|   (Frontend)      |                    |   (Middleware)    |                     | (Microcontroller)  |
|                   |                    |                   |                     |      eg.pico       |
+-------------------+                    +-------------------+                     +-------------------+
        ^                                         ^                                         ^
        |                                         |                                         |
        |                                         |                                         |
        |                                         |                                         |
        |                                         |                                         |
        |                                         |                                         |
        +-----------------------------------------+-----------------------------------------+
                                      Debugging Workflow
```
