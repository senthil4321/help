# Yocto commands
### Commands Raspberry pi image creation
```
bitbake rpi-basic-image
bitbake -g -u taskexp core-image-minimal
```
### working directory 
```
WORKDIR the recipe’s working directory

S The directory where the source code is extracted

B The directory where bitbake places the objects generated during the
build

D The destination directory (root directory of where the files are
installed, before creating the image).
```

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
