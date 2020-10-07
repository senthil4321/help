# Batchfile creation
## for loop
```
FOR /L %N IN () DO @echo looping && @adb wait-for-device && adb forward tcp:3490 tcp:3490 && adb shell
```
### Example Command Line 2
```
for /f "tokens=2 delims==" %a in ('wmic OS Get localdatetime /value') do set "dt=%a"
```
### Example Batch File
```
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
```
### Example Batch File 1
```
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "YY=%dt:~2,2%" & set "YYYY=%dt:~0,4%" & set "MM=%dt:~4,2%" & set "DD=%dt:~6,2%"
set "HH=%dt:~8,2%" & set "Min=%dt:~10,2%" & set "Sec=%dt:~12,2%"

set "datestamp=%YYYY%%MM%%DD%" & set "timestamp=%HH%%Min%%Sec%"
set "fullstamp=%YYYY%-%MM%-%DD%_%HH%-%Min%-%Sec%"
echo datestamp: "%datestamp%"
echo timestamp: "%timestamp%"
echo fullstamp: "%fullstamp%
```
### Ref.
https://ss64.com/nt/for_f.html

## Percentage symbol usage in command line and batch file
```
   %%parameter    A replaceable parameter:              
                  in a batch file use %%G (on the command line %G)
```
## Variable Handling
1. https://stackoverflow.com/questions/3068929/how-to-read-file-contents-into-a-variable-in-a-batch-file  
1. https://stackoverflow.com/questions/28133052/saving-a-batch-variable-in-a-text-file  

## Exit code
```
exit /b %ERRORLEVEL%
```
* https://www.manageengine.com/products/desktop-central/batch-file-errorlevels.html
### pass parameters
```
demo.bat data1

echo %1%
```
## comments
```
REM Remarks comment
:: Demo comment
```
### comport 
* https://www.google.com/amp/s/batchloaf.wordpress.com/2013/02/12/simple-trick-for-sending-characters-to-a-serial-port-in-windows/amp/
