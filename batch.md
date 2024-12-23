# Batchfile creation
## for loop
```bat
FOR /L %N IN () DO @echo looping && @adb wait-for-device && adb forward tcp:3490 tcp:3490 && adb shell
```
### Example Command Line 2
```bat
for /f "tokens=2 delims==" %a in ('wmic OS Get localdatetime /value') do set "dt=%a"
```
### Example Batch File
```bat
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
```
### Example Batch File 1
```bat
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
```bat
   %%parameter    A replaceable parameter:              
                  in a batch file use %%G (on the command line %G)
```
## Variable Handling
1. https://stackoverflow.com/questions/3068929/how-to-read-file-contents-into-a-variable-in-a-batch-file  
1. https://stackoverflow.com/questions/28133052/saving-a-batch-variable-in-a-text-file  

## Drive path from the parameter
```bat
%~dp0
```
### Ref
* https://stackoverflow.com/questions/112055/what-does-d0-mean-in-a-windows-batch-file
* https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-xp/bb490909(v=technet.10)?redirectedfrom=MSDN
## Exit code
```bat
exit /b %ERRORLEVEL%
```
* https://www.manageengine.com/products/desktop-central/batch-file-errorlevels.html
### pass parameters
```bat
demo.bat data1

echo %1%
```
## comments
```
REM Remarks comment
:: Demo comment
```
### comport 
```bat
set /p x="1" <nul >\\.\COM2
mode COM22 BAUD=9600 PARITY=n DATA=8
```
* https://www.google.com/amp/s/batchloaf.wordpress.com/2013/02/12/simple-trick-for-sending-characters-to-a-serial-port-in-windows/amp/
* https://batchloaf.wordpress.com/2013/02/12/simple-trick-for-sending-characters-to-a-serial-port-in-windows/
### com0com
* https://pete.akeo.ie/2011/07/com0com-signed-drivers.html
### echo without newline
```bat
echo|set /p="Hello World"
```
* https://stackoverflow.com/questions/7105433/windows-batch-echo-without-new-line
### git bash
git bash in windows is slow but very good. Used it to check folder using more space. 
### if exist
This command is used to check if file or directory exist and executes command.
```cmd
if exist c:\logs 7z.exe c:\logs
```
* https://stackoverflow.com/questions/4340350/how-to-check-if-a-file-exists-from-inside-a-batch-file
### auto close bat after time out
```bat
@timeout /T 10 /nobreak
```
### Example 1 return error code
```bat
date /t
set /A EC1=%ErrorLevel%
if %ErrorLevel% == 0 (
date /t
)
set /A EC2=%ErrorLevel%  
date1 /t
set /A EC="%EC1%|%EC2%|%ErrorLevel%"

ECHO Result Code: %ErrorLevel%
ECHO Result Code: %EC%
EXIT /B %EC% 
```
### Example 2 return error code
```bat
date /t
if %ErrorLevel% == 0 (
echo "No Error"    
)
ECHO Result Code: %ErrorLevel%
exit /b %errorlevel%
```
### bat file to launch program in loop
```batch
```
#### 
* https://stackoverflow.com/questions/9344235/how-to-restart-program-automatically-if-it-crashes-in-windows
