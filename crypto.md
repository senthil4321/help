## aes cuda
* https://developer.nvidia.com/gpugems/gpugems3/part-vi-gpu-computing/chapter-36-aes-encryption-and-decryption-gpu
## cyber security
* https://www.google.com/url?sa=t&source=web&rct=j&url=https://wiki.yoctoproject.org/wiki/images/archive/0/0d/20200702141904%2521DD5_Security_Hardening_NA20.pdf&ved=2ahUKEwj4gIaewfzwAhWL3eAKHSq2DNEQFjAFegQIHRAC&usg=AOvVaw0zfF9uv_Iog493T6bbnPI4
## HMAC
### Yocto TPM
* https://ubs_csse.gitlab.io/secu_os/tutorials/tpm_rpi.html
* https://bootlin.com/blog/measured-boot-with-a-tpm-2-0-in-u-boot/
### Enable TPM support in uboot
```
make menuconfig
```
* https://github.com/joholl/rpi4-uboot-tpm
---
## NON TPM Implementation
## Raspberry Pi Secure Boot --- Keystored in SD Card
* https://blog.nviso.eu/2019/04/01/enabling-verified-boot-on-raspberry-pi-3/

## Compiline U Boot
* https://www.beyondlogic.org/compiling-u-boot-with-device-tree-support-for-the-raspberry-pi/

### Link to Uboot Source
https://ftp.denx.de/pub/u-boot/

### Steps to compile Uboot
### Link to Uboot Source
https://ftp.denx.de/pub/u-boot/

### Steps to compile Uboot
#### Tools needed
```bash
sudo apt-get install flex bison
```
```bash
wget https://ftp.denx.de/pub/u-boot/u-boot-2022.01.tar.bz2
tar -xjf u-boot-2022.01.tar.bz2
cd u-boot-2022.01
make distclean
make rpi_2_defconfig

```


#### Raspberry Pi Boot Process with picture
* https://argus-sec.com/raspberry-pi-remote-flashing/

## Linux commands
```
lsblk -a -f

```
### umount
```
umount /mnt/srkfs
or 
umount /dev/sda1 /mnt/srkfs
```

```
${kernel_addr_r} 

setenv bootcmd 'fatload mmc 0 ${kernel_addr_r} Image ; fatload mmc 0 ${fdt_addr_r} bcm2709-rpi-2-b.dtb ; booti ${kernel_addr_r} - ${fdt_addr_r}'



bcm2708-rpi-0-w.dtb:      Pi Zero W
bcm2708-rpi-b.dtb:        Pi Model B and Model A
bcm2708-rpi-b-plus.dtb:   Pi B+, A+ and Zero
bcm2708-rpi-cm.dtb:       Compute Module (a minimal dtb, intended to be a starting point)
bcm2709-rpi-2-b.dtb:      Pi 2B
bcm2710-rpi-3-b.dtb:      Pi 3B
bcm2710-rpi-3-b-plus.dtb: Pi 3B+ and 3A+
bcm2710-rpi-cm3.dtb:      Compute Module 3



setenv bootcmd 'fatload mmc 0 ${kernel_addr_r} Image ; fatload mmc 0 ${fdt_addr_r} bcm2837-rpi-3-b-plus.dtb ; booti ${kernel_addr_r} - ${fdt_addr_r}'


fatload usb 0:1 0x80200000 uImage 
fatload usb 0:1 0x80e00000 am335x-evm.dtb
bootm 0x80200000 - 0x80e00000 

fatload mmc 0:1 ${kernel_addr_r} kernel7.img
bootm ${kernel_addr_r} - ${fdt_addr_r}
mmc dev 0

fatload mmc 0:1 ${kernel_addr_r} kernel7.img
fatload mmc 0:1 ${fdt_addr_r} bcm2709-rpi-2-b.dtb 
setenv bootargs earlyprintk console=ttyAMA0 console=tty1 root=/dev/mmcblk0p2 rootwait
bootz ${kernel_addr_r} - ${fdt_addr_r}

Raspberry pi kenerel Image namiing
kernel.img piv1
kernel7.img piv2
https://forums.raspberrypi.com/viewtopic.php?t=187136


Hardware        : BCM2835
Revision        : a01041
Serial          : 000000008e8c5bd6
Model           : Raspberry Pi 2 Model B Rev 1.1

 
bcm2836-rpi-2-b.dtb

 
 ls mmc 0:1
 ```
 ### Ref.
 * https://www.thegoodpenguin.co.uk/blog/build-boot-linux-on-raspberry-pi-3-model-b/
### Why Raspberri pi cpuinfo hardware is wrong ?
It is because of the Linux Kernel to keep things simple. Use `Revision        : a01041` to determine version.
### Device tree version and Revision from cpuinfo is different.
>>> For Model `Raspberry Pi 2 Model B Rev 1.1` device tree version is bcm2709-rpi-2-b.dtb

