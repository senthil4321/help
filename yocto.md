# Yocto commands
## 
> [!IMPORTANT]
> DISTRO_FEATURES  
MACHINE_FEATURES  
IMAGE_FEATURES  

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
bitbake-getvar -r core-image-minimal S
bitbake-getvar -r core-image-minimal B
bitbake-getvar -r core-image-minimal D
```
> ${BPN}-${PV}
```
bitbake-getvar -r core-image-minimal BPN
bitbake-getvar -r core-image-minimal PN
```
* https://wiki.koansoftware.com/index.php/How_to_trace_a_variable_setting_with_bitbake-getvar

```bash
bitbake-getvar DISTRO_FEATURES
bitbake-getvar MACHINE_FEATURES
bitbake-getvar IMAGE_FEATURES
bitbake-getvar INIT_MANAGER
```
## Kernel Optimisation
## Kernel Config and Compilation
```
bitbake -c menuconfig virtual/kernel
```
```
bitbake virtual/kernel
```
```
bitbake-getvar DISTRO_FEATURES
```
> DISTRO_FEATURES:remove = " ipv4"
### View dependecy tree
```
bitbake -g -u taskexp core-image-minimal
```
### List tasks virtual kernel
```
bitbake -c listtasks virtual/kernel
bitbake -c menuconfig virtual/kernel
bitbake -c diffconfig virtual/kernel
bitbake -c cleansstate virtual/kernel
bitbake -c kernel_configcheck -f virtual/kernel
```
* https://wiki.koansoftware.com/index.php/Modify_the_linux_kernel_with_configuration_fragments_in_Yocto
  
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
> CTRL + ALT + 1  
> CTRL + ALT + 2  
> CTRL + ALT + 3  
```
runqemu core-image-minimal
```
## Testing 
```bash
bitbake -c testimage image
```
* https://docs.yoctoproject.org/dev-manual/runtime-testing.html#performing-automated-runtime-testing
---
### working directory 
`WORKDIR` the recipe’s working directory
`S` The directory where the source code is extracted
`B` The directory where bitbake places the objects generated during the
build
`D` The destination directory (root directory of where the files are
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
  
## 
### How to change Init Manager ?
#### Available Options
```
sysvinit
systemd
mdev-busybox
```
* https://wiki.koansoftware.com/index.php/Add_a_systemd_service_file_into_a_Yocto_image
* https://docs.yoctoproject.org/dev/ref-manual/variables.html#term-INIT_MANAGER
* https://docs.yoctoproject.org/dev/dev-manual/init-manager.html
* https://docs.yoctoproject.org/dev/dev-manual/init-manager.html#init-manager
### Linux runlevel
## Poky-tiny
1. Image build sucess
2. poky/meta-poky/conf/distro/poky-tiny.conf
3. poky/meta/recipes-kernel/linux/linux-yocto-tiny_6.6.bb
* https://wiki.yoctoproject.org/wiki/Poky-Tiny
  
### Command to start QEMU
```
runqemu core-image-minimal
```
### Meaning of grep
```
ps |grep -v [[]
-v invert match
[] regex
[ item to search in regex
```
---
## Kernel Size Analysis
### Location of Kernel Build Directory
```
~/project/poky/build/tmp/work/qemux86_64-poky-linux-musl/linux-yocto-tiny/6.10.11+git/linux-qemux86_64-tiny-build$ ~/project/poky/scripts/tiny/ksize.py 
```
```
cd ~/project/poky/build/tmp/work/qemux86_64-poky-linux-musl/linux-yocto-tiny/6.10.11+git/linux-qemux86_64-tiny-build
```
## TODO Read
1. https://wiki.koansoftware.com/index.php/Add_a_systemd_service_file_into_a_Yocto_image
2. https://docs.yoctoproject.org/dev/ref-manual/variables.html#term-INIT_MANAGER
3. https://docs.yoctoproject.org/dev/dev-manual/init-manager.html
4. https://docs.yoctoproject.org/dev/dev-manual/init-manager.html#init-manager
5. https://docs.yoctoproject.org/ref-manual/features.html
```
bitbake -g core-image-minimal
```
### How to know which append files are used in the build ? 
```
bitbake-layers show-appends
```
* https://stackoverflow.com/questions/32850160/bitbake-how-to-list-all-recipe-and-append-files-used-in-an-image
  
## View Package genereated by recipe

### Build the Recipe:

```bash
bitbake srk-init-folder
```

### List All Packages Generated by the Recipe:

```bash
oe-pkgdata-util list-pkgs | grep srk-init-folder
```

### List Files in the Package:

```bash
oe-pkgdata-util list-pkg-files srk-init-folder
```
### Show Detailed Information About the Package:

```bash
oe-pkgdata-util list-pkg-info srk-init-folder
```
### Summary

By using the oe-pkgdata-util tool, you can view the contents of a package generated by a Yocto recipe. This tool allows you to query the package data and see which files are included in a specific package, providing valuable insights into the contents of your Yocto image.

### How to find the recipe which provide the file ?

```bash
oe-pkgdata-util find-path /usr/bin/hello
```

#### Example Flow
```bash
oe-pkgdata-util find-path /etc/inittab
#Example output
/etc/inittab: base-files
#Finding the Recipe
find meta* -name "busybox-inittab*.bb"
```

### How to find how a particular variable is set ?

```bash
bitbake -e core-image-tiny-initramfs-srk-3 |grep -n -A 10 ^VIRTUAL-RUNTIME_init_manager
```
### Different types of init scripts

```bash
VIRTUAL-RUNTIME_initscripts ??= "initscripts"
VIRTUAL-RUNTIME_initscripts = "busybox-initscripts"
```
### Different types of libc
```bash
PREFERRED_PROVIDER_virtual/libc = "glibc"#default
PREFERRED_PROVIDER_virtual/libc = "musl"#light weight
PREFERRED_PROVIDER_virtual/libc = "uclibc"#not used much
```

### How to create patch
Always create patches from the exact kernel source version used in Yocto.
Use git diff or git format-patch from a kernel repo checked out at the same commit Yocto uses.

Perfect 👍 — here’s the **full tree diagram + BitBake task timeline** for your `bbb-01-eeprom` recipe inside Yocto:

---

```text
/home/srk2cob/project/poky/
│
├── build/
│   └── tmp/
│       ├── work/
│       │   └── beaglebone-poky-linux-gnueabi/
│       │       └── bbb-01-eeprom/1.0-r0/    # ${WORKDIR}
│       │           ├── sources/             # ${S} (from do_unpack)
│       │           │   └── bbb-01-eeprom.c
│       │           ├── temp/                # Logs + run files for each task
│       │           │   ├── log.do_fetch
│       │           │   ├── log.do_unpack
│       │           │   ├── log.do_patch
│       │           │   ├── log.do_compile
│       │           │   ├── log.do_install
│       │           │   ├── log.do_package
│       │           │   └── ...
│       │           ├── image/               # ${D} (from do_install)
│       │           │   └── usr/bin/
│       │           │       └── bbb-01-eeprom
│       │           └── recipe-sysroot/      # Build-time sysroot
│       │
│       ├── deploy/
│       │   ├── ipk/armv7a/
│       │   │   └── bbb-01-eeprom_1.0-r0_armv7a.ipk   # Final package
│       │   └── images/beaglebone/
│       │       └── core-image-minimal-beaglebone.ext4
│       │       └── core-image-minimal-beaglebone.tar.gz
│       │
│       └── cache/    # Shared parsing cache
│
└── meta-srk/
    └── recipes-bsp/
        └── bbb-01-eeprom/
            └── bbb-01-eeprom.bb
```

---

### 🔑 BitBake Task Timeline for `bbb-01-eeprom`

1. **`do_fetch`**

   * Pulls sources from `SRC_URI` → places them in `${DL_DIR}`.

2. **`do_unpack`**

   * Extracts sources → `${WORKDIR}/sources/`.

3. **`do_patch`**

   * Applies patches (if `SRC_URI` contains `.patch` files).

4. **`do_configure`**

   * Runs configure step (for autotools/cmake/etc).
   * For your simple recipe, might be skipped.

5. **`do_compile`**

   * Builds sources → produces binary `bbb-01-eeprom`.

6. **`do_install`**

   * Installs into staging directory `${D}` (→ `${WORKDIR}/image/`).

7. **`do_package`**

   * Splits installed files into packages (`${PN}`, `${PN}-dbg`, etc.).

8. **`do_package_write_ipk` / `do_package_write_rpm` / `do_package_write_deb`**

   * Creates the actual `.ipk/.deb/.rpm` under `tmp/deploy/`.

9. **`do_rootfs`**

   * Pulls required packages into the root filesystem.

10. **`do_image`**

    * Generates final image files (`.ext4`, `.wic`, `.tar.gz`).

---

⚡ So: `bbb-01-eeprom.c` → `${WORKDIR}/sources/` → compile → `${D}/usr/bin/` → package (`ipk`) → deployed into final BeagleBone image.

Would you like me to **make this into an SVG pipeline diagram** (boxes with arrows: fetch → unpack → patch → compile → install → package → rootfs → image) so you can use it in documentation?

