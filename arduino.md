# arduino

Documentation for Arduino hardwae and software components.
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
> This section has the documentaiton for tonuino development kit.
> It is important to add the 1k ohm resistor to the Rx line to remove the noise in the speaker

* https://github.com/xfjx/TonUINO

### DF Player
use the below name to search for DFMiniMp3 in arduion library search
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
