# arduino

## Circuit theory
Any passive electrical circuit can be built only with passive component resistor, capacitor and inductor.

### What is passive circuit?

A passive circuit:
1. Does not store energy???
2. Does not generate energy
3. Does not require external power to operate

### Ref
1. https://www.youtube.com/watch?v=FhmLb2DhNYM&t=579s

## Documentation for Arduino hardware and software components.
## Insert Date time during startup
```c
const char compile_date[] = __DATE__ " " __TIME__;
const char compile_date[] = "Sep 22 2013 01:19:49";
```
### Ref.
* https://forum.arduino.cc/t/arduino-ide-get-current-date-at-compile-time-and-insert-into-sketch/184602/3
### auto reset
* https://electronics.stackexchange.com/questions/351120/auto-reset-an-arduino-using-ftdi-dtr-signal-stays-low-and-needs-to-go-high-aft

---
## Tonuino
> This section has the documentation for tonuino development kit.
> It is important to add the 1k ohm resistor to the Rx line to remove the noise in the speaker

* https://github.com/xfjx/TonUINO

### DF Player
use the below name to search for DFMiniMp3 in arduino library search
```
DFPlayer Mini Mp3 by Makuna
```
* https://github.com/Makuna/DFMiniMp3
* https://wiki.dfrobot.com/DFPlayer_Mini_SKU_DFR0299

Sound issue
* https://arduino.stackexchange.com/questions/49807/dfplayer-noise-researched-tried-and-bep-bep-bep-bep-bep/49842#49842

### JC Button
```
JC_Button
```
* https://github.com/JChristensen/JC_Button
### MFRC522
```
MFRC522
```
#### Data sheet
Card
* https://www.nxp.com/docs/en/data-sheet/MF1S50YYX_V1.pdf
Reader
* https://www.nxp.com/docs/en/data-sheet/MFRC522.pdf
### wiring diagram
* https://github.com/senthil4321/TonUINO/blob/master/TonUINO_Schaltplan.pdf
---
## op amp
* https://forum.arduino.cc/index.php?topic=438366.0

## raspberry pico

* https://learnembeddedsystems.co.uk/basic-multicore-pico-example
## byte array init
* https://stackoverflow.com/questions/33454988/c-initialize-array-in-hexadecimal-values
## dlt
* https://www.embeddedtutor.com/2021/04/watchdog-manager-in-autosar.html?m=1
### Minimal Atmelmeaga8 Worked
* http://www.gammon.com.au/breadboard
* https://github.com/nickgammon/arduino_sketches
#### other
* https://todbot.com/blog/2009/05/26/minimal-arduino-with-atmega8/comment-page-5/
 * https://anwarstech.wordpress.com/2018/01/15/how-to-setup-a-low-power-atmega8-microcontroller/
### Arduino Low power Atmel mega8
* https://learn.sparkfun.com/tutorials/reducing-arduino-power-consumption

### camera
* http://embeddedprogrammer.blogspot.com/2012/07/hacking-ov7670-camera-module-sccb-cheat.html

### 24 awg wire for hobby
* https://www.ftdichip.com/Support/Documents/DataSheets/Cables/DS_TTL-232RG_CABLES.pdf

### Current Measuremet
* https://circuitdigest.com/microcontroller-projects/precision-digital-micro-current-meter
