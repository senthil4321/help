# Yocto commands
### Commands Raspberry pi image creation
```
bitbake rpi-basic-image
```
### devshell
```
bitbake -c devshell hello
```
### bitbake-getvar 
```
bitbake-getvar [-h] [-r RECIPE] [-u] [-f FLAG] [--value] variable
```
```
bitbake-getvar DEPLOY_DIR
bitbake-getvar IMAGE_FSTYPES
bitbake-getvar IMAGE_INSTALL
bitbake-getvar MACHINE
```
```
itbake-getvar -r core-image-minimal S
itbake-getvar -r core-image-minimal B
itbake-getvar -r core-image-minimal D
```
> ${BPN}-${PV}
```
bitbake-getvar -r core-image-minimal BPN
bitbake-getvar -r core-image-minimal PN
```
* https://wiki.koansoftware.com/index.php/How_to_trace_a_variable_setting_with_bitbake-getvar

### View dependecy tree
```
bitbake -g -u taskexp core-image-minimal
```
### List tasks virtual kernel
```
bitbake -c listtasks virtual/kernel
bitbake -c menuconfig virtual/kernel
```
### Force run all tasks
```
bitbake -f hello
```
### download source
```
bitbake --runall=fetch core-image-minimal
```
### show all recipes 
```
bitbake -s
```
### Showlayers
```
bitbake-layers show-layers
```
### Add-layer
```
bitbake-layers add-layer meta-srk
bitbake-layers remove-layer meta-srk
```
## qemu
> [!NOTE]
CTRL + ALT + 1
CTRL + ALT + 2
CTRL + ALT + 3

```
runqemu core-image-minimal
```
* 
## Testing 
```bash
bitbake -c testimage image
```
* https://docs.yoctoproject.org/dev-manual/runtime-testing.html#performing-automated-runtime-testing
---
### working directory 

WORKDIR the recipe’s working directory

S The directory where the source code is extracted

B The directory where bitbake places the objects generated during the
build

D The destination directory (root directory of where the files are
installed, before creating the image).

## oe-pkgdata-util
### what recipe is creating
```
oe-pkgdata-util list-pkg-files busybox
```
```
oe-pkgdata-util list-pkg-files hello
```
### which recipe creates the package
```
oe-pkgdata-util lookup-recipe hello
```
## Variables
### CC
> The minimal command and arguments used to run the C compiler.

### CC
> The minimal command and arguments used to run the C compiler.
### CFLAGS
> Specifies the flags to pass to the C compiler.
### CXX
> The minimal command and arguments used to run the C++ compiler.
### CXXFLAGS
> Specifies the flags to pass to the C++ compiler.

### Yocto
* https://tutorialadda.com/yocto/yocto-hello-world-recipe-compile-using-makefile

### Yocoto Newversion Changes
> ~~IMAGE_INSTALL_append += " hello"~~
> IMAGE_INSTALL:append += " hello"
---
### Tutorial
* https://tutorialadda.com/yocto/create-a-new-meta-layer-and-write-new-recipe-in-yocto-project

### Analysis
* https://github.com/yoctoproject/poky/blob/master/meta-poky/conf/distro/poky.conf
* https://github.com/yoctoproject/poky/blob/master/meta-poky/conf/distro/poky-tiny.conf

Below reipes provide the logic to download the kernel based on architecture and machine

* https://github.com/yoctoproject/poky/blob/master/meta/recipes-kernel/linux/linux-yocto_5.15.bb
* https://github.com/yoctoproject/poky/blob/master/meta/recipes-kernel/linux/linux-yocto-tiny_5.15.bb

* https://github.com/yoctoproject/poky/blob/master/meta-yocto-bsp/conf/machine/beaglebone-yocto.conf

### Kernel Source
* https://git.yoctoproject.org/linux-yocto/
#### Other
* https://git.yoctoproject.org/poky/plain/meta/recipes-kernel/linux/linux-yocto-tiny_5.15.bb
* https://github.com/yoctoproject/poky/blob/92bb6f72ceb39c99e5c93c0a99b70fb210233acb/meta-yocto-bsp/conf/machine/beaglebone-yocto.conf

### Kernel Source local file system
```
~/project/help/poky/build/tmp/work/beaglebone_yocto-poky-linux-gnueabi/linux-yocto/5.15.36+gitAUTOINC+947149960e_4c875cf137-r0
```
* https://git.yoctoproject.org/linux-yocto/refs/
* https://git.yoctoproject.org/linux-yocto/log/?h=v5.15/standard/beaglebone

git source url and the git path in the server mathes
```
SRC_URI = "git://git.yoctoproject.org/linux-yocto.git;branch=${KBRANCH};name=machine \
           git://git.yoctoproject.org/yocto-kernel-cache;type=kmeta;name=meta;branch=yocto-5.15;destsuffix=${KMETA}"
```
### bitbake gui
* https://wiki.yoctoproject.org/wiki/BitBake/GUI

### Yocto Installation
* https://docs.yoctoproject.org/ref-manual/system-requirements.html#required-packages-for-the-build-host
  
