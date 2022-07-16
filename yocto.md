# Yocto commands
### Commands Raspberry pi image creation
```
bitbake rpi-basic-image
bitbake -g -u taskexp core-image-minimal
```
### working directory 
WORKDIR the recipe’s working directory
S The directory where the source code is extracted
B The directory where bitbake places the objects generated during the
build
D The destination directory (root directory of where the files are
installed, before creating the image).
