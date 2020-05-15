# Batchfile creation
## for loop
```
FOR /L %N IN () DO @echo looping && @adb wait-for-device && adb forward tcp:3490 tcp:3490 && adb shell
```
## Variable Handling
1. https://stackoverflow.com/questions/3068929/how-to-read-file-contents-into-a-variable-in-a-batch-file  
1. https://stackoverflow.com/questions/28133052/saving-a-batch-variable-in-a-text-file  
