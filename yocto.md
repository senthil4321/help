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

* https://github.com/yoctoproject/poky/blob/master/meta/recipes-kernel/linux/linux-yocto_5.15.bb
* https://github.com/yoctoproject/poky/blob/master/meta/recipes-kernel/linux/linux-yocto-tiny_5.15.bb


* https://github.com/yoctoproject/poky/blob/master/meta-yocto-bsp/conf/machine/beaglebone-yocto.conf
#### Other
* https://git.yoctoproject.org/poky/plain/meta/recipes-kernel/linux/linux-yocto-tiny_5.15.bb
* https://github.com/yoctoproject/poky/blob/92bb6f72ceb39c99e5c93c0a99b70fb210233acb/meta-yocto-bsp/conf/machine/beaglebone-yocto.conf
