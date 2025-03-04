# Linux

## Table of Contents

- [Shell Script](#shell-script)
  - [Redirection](#redirection)
- [od](#od)
- [awk](#awk)
  - [Variable and String](#variable-and-string)
    - [When We Need Curly Braces Around Shell Variables](#when-we-need-curly-braces-around-shell-variables)
  - [Parameter Expansion](#parameter-expansion)
- [Variable Parameter](#variable-parameter)
- [Globbing File Expansion](#globbing-file-expansion)
- [Shell Redirection](#shell-redirection)
- [curl](#curl)
- [Change Hostname of Linux System](#change-hostname-of-linux-system)
- [Passing Password to scp ssh](#passing-password-to-scp-ssh)
- [dmesg](#dmesg)
- [udev](#udev)
- [Remount Read Write](#remount-read-write)
- [top](#top)
- [History](#history)
  - [Enable Unlimited Command History](#enable-unlimited-command-history)
  - [Enable Immediate History Saving](#enable-immediate-history-saving)
  - [Search Long Commands in History](#search-long-commands-in-history)
  - [History Run with Command Number](#history-run-with-command-number)
- [SCP](#scp)
  - [Copy from Remote PC](#copy-from-remote-pc)
- [Linux Shell Commands Redirection to Multiple Places](#linux-shell-commands-redirection-to-multiple-places)
- [Raspberry Pi](#raspberry-pi)
  - [Configure Network](#configure-network)
  - [Command to Update the Config](#command-to-update-the-config)
  - [Enable Time Information in History](#enable-time-information-in-history)
- [dm-verity](#dm-verity)
  - [Preparing Block Device](#preparing-block-device)
  - [Mounting and Checking Verity](#mounting-and-checking-verity)
- [Secure Boot](#secure-boot)
- [Overlay FS](#overlay-fs)
- [Coredump](#coredump)
- [IPK](#ipk)
- [Bash Script](#bash-script)
  - [Bash Script - Give Input to Program Linux](#bash-script---give-input-to-program-linux)
  - [Search for Text in Files](#search-for-text-in-files)
- [Search](#search)
- [xxd](#xxd)
- [Guidelines](#guidelines)
- [String Handling](#string-handling)
- [Array [@]](#array-@)
- [Bash Script](#bash-script)
  - [Difference Between Double and Single Quotes](#difference-between-double-and-single-quotes)
  - [Bash Glob](#bash-glob)
  - [Bracket If Condition](#bracket-if-condition)
  - [Tutorial](#tutorial)
  - [Regex Operation =~](#regex-operation-~)
  - [String Compare Regex](#string-compare-regex)
- [Switch Case](#switch-case)
  - [Double Semicolon](#double-semicolon)
  - [Option and Parameter](#option-and-parameter)
  - [Substring Remove](#substring-remove)
  - [Parameter Search and Replace](#parameter-search-and-replace)
- [sed](#sed)
- [Command to Ignore the HUP (Hangup) Signal](#command-to-ignore-the-hup-hangup-signal)
- [ifconfig](#ifconfig)
- [CAN Tools](#can-tools)
- [Install libc6](#install-libc6)
- [Running Commands One After Another](#running-commands-one-after-another)
- [Cron Job](#cron-job)
- [sort](#sort)
- [Get First Line](#get-first-line)
- [du](#du)
- [chown and chmod](#chown-and-chmod)
- [Raspi WiFi USB Dongle Setup](#raspi-wifi-usb-dongle-setup)
- [Streaming](#streaming)
- [Autostart Octoprint in Ubuntu Server](#autostart-octoprint-in-ubuntu-server)
- [How to Find the Program Location?](#how-to-find-the-program-location)
- [Convert Windows Path to Linux](#convert-windows-path-to-linux)
- [Linux cd to Previous Directory](#linux-cd-to-previous-directory)
- [qwe Bookmark Directory](#qwe-bookmark-directory)
- [alias](#alias)
- [Linux File System](#linux-file-system)
- [Useful](#useful)
- [Useful Programs](#useful-programs)
- [Ethernet Interface Naming](#ethernet-interface-naming)
- [Linux Expand Partition](#linux-expand-partition)
- [zcat](#zcat)
- [zgrep](#zgrep)
- [tree](#tree)
- [epoll](#epoll)
- [put cursor at the bottom of the screen](#put-cursor-at-the-bottom-of-the-screen)
- [Setting SWAP](#setting-swap)

## Shell Script

### Redirection

`<<<` is not supported by sh.

### Ref.

1. https://unix.stackexchange.com/questions/208911/while-read-loop
1. [Link2](http://www.compciv.org/topics/bash/variables-and-substitution/#:~:text=From%20the%20Bash%20documentation%3A,with%20any%20trailing%20newlines%20deleted.)

## od

Print file in hex and other formats. With no FILE, or when FILE is -, read standard input.

RADIX is d for decimal, o for octal, x for hexadecimal or n for none.

```bash
od -x 
```

### Ref.

[Manpage](https://man7.org/linux/man-pages/man1/od.1.html)

## awk

### Variable and String

#### When We Need Curly Braces Around Shell Variables

#### Ref.

1. https://stackoverflow.com/questions/8748831/when-do-we-need-curly-braces-around-shell-variables

### Parameter Expansion

* https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html
* https://wiki.bash-hackers.org/syntax/pe

## Variable Parameter

A parameter is an entity that stores values.

## Globbing File Expansion

Bash does carry out filename expansion, a process known as globbing, but this does not use the standard RE set. Instead, globbing recognizes and expands wild cards. Globbing interprets the standard wild card characters: * and ?, character lists in square brackets, and certain other special characters (such as ^ for negating the sense of a match).
* https://tldp.org/LDP/abs/html/globbingref.html

## Shell Redirection

* https://unix.stackexchange.com/questions/159513/what-are-the-shells-control-and-redirection-operators

## curl

curl is also available in Windows.

`@` before file\
`@-` to read from stdin

Use `-u` option to pass username and password\
Use `-C -` option to skip already downloaded info.

### Ref.

* https://stackoverflow.com/questions/11856351/how-to-skip-already-existing-files-when-downloading-with-curl

## Change Hostname of Linux System

Edit the below file to update the hostname of the Linux system.

```bash
/etc/hostname
```

## Passing Password to scp ssh

Switch to key-based authentication.

```bash
sshpass -p "password" scp -r user@example
sudo apt-get install sshpass
sshpass -p password ssh user@hostname
```

## dmesg

Prints the message buffer of the kernel. Contains messages from device drivers.

## udev

**udev** is a Linux subsystem to handle device events. It enables triggering scripts when a device is plugged in.

### Ref.

1. https://stackoverflow.com/questions/7172784/how-do-i-post-json-data-with-curl
1. https://stackoverflow.com/questions/12583930-use-pipe-for-curl-data

## Remount Read Write

```bash
sudo fdisk -l
sudo mount -o remount,rw /dev/sdc1
```

## top

Program to get CPU and memory usage.

```bash
top 
```

## History

### Enable Unlimited Command History

```bash
HISTSIZE=-1 
HISTFILESIZE=-1
```

### Enable Immediate History Saving

Place the below line in the ~/.bash_rc or ~/.bashrc.

```bash
export PROMPT_COMMAND='history -a'
```

### Search Long Commands in History

```bash
CTRL + R
```

### History Run with Command Number

```bash
!550 runs the command with number 550. Use 'history' to get the number.
!-2 
```

## SCP

### Copy from Remote PC

```bash
scp username@192.168.0.172:/remote/file.txt ./
```

### Ref.

* https://my.esecuredata.com/index.php?/knowledgebase/article/21/copying-multiple-files-at-the-same-time-using-scp

## Linux Shell Commands Redirection to Multiple Places

```bash
echo "SRK fdisk complete" | tee /dev/kmsg | tee /dev/ttyHSL0
```

## Raspberry Pi 

### Configure Network

```yaml
network:
    version: 2
    ethernets:
        eth0:
            match:
                macaddress: <MAC>
            set-name: eth0
            addresses:               
                - 192.168.0.162/24
            gateway4: 192.168.0.1
    wifis:
        wlan0:
            optional: true
            access-points:
                "XXXXXXX":
                   password: "XXXXX"
            addresses:
                - 192.168.0.172/24
```

### Command to Update the Config

```bash
sudo netplan --debug try
sudo netplan --debug generate 
sudo netplan --debug apply
```
### Ref.
1. https://raspberrypi.stackexchange.com/questions/98598/how-to-setup-the-raspberry-pi-3-onboard-wifi-for-ubuntu-server-18-04-with-netpla

### Enable Time Information in History

```bash
echo 'HISTTIMEFORMAT="%d/%m/%y %T "' >> ~/.bashrc 
source ~/.bashrc
```

### Ref.

1. https://unix.stackexchange.com/questions/145250/where-is-bashs-history-stored
1. https://askubuntu.com/questions/391082/how-to-see-time-stamps-in-bash-history

## dm-verity

### Preparing Block Device

```bash
dd if=/dev/zero of=./diskimage bs=1M count=10
dd if=/dev/zero of=./dm-hash bs=1M count=10

sudo mount -o loop=/dev/loop17 ./diskimage /mnt/dm-srk-img/
sudo touch /mnt/dm-srk-img/hello.txt
sudo umount /mnt/dm-srk-img/
sudo losetup /dev/loop17 ./dm-hash
sudo losetup /dev/loop18 ./diskimage
```

### Mounting and Checking Verity

```bash
sudo --debug veritysetup format /dev/loop18 /dev/loop17
sudo veritysetup --debug create dm-romfs /dev/loop18 /dev/loop17 9158af2ae47a9e0029765ec242b1d68357b58143802bcff430b3b4957bb28004
sudo veritysetup --debug close dm-romfs
sudo veritysetup --debug status dm-romfs
sudo veritysetup --debug verify /dev/loop18 /dev/loop17 9158af2ae47a9e0029765ec242b1d68357b58143802bcff430b3b4957bb28004
```

* https://github.com/shakna-israel/cryptsetup/issues/204
* https://source.android.com/security/verifiedboot/dm-verity#mapping-table
* https://man7.org/linux/man-pages/man8/veritysetup.8.html
* https://www.jamescoyle.net/how-to/2096-use-a-file-as-a-linux-block-device

## Secure Boot

* https://elinux.org/images/e/e0/Josserand-schulz-secure-boot.pdf

## Overlay FS

```bash
mount -t overlay overlay -o lowerdir=/usr/bin,upperdir=/mnt/mmc/usr/bin_upper,workdir=/mnt/mmc/wordir /usr/bin
```

* https://www.datalight.com/blog/2016/01/27/explaining-overlayfs-%E2%80%93-what-it-does-and-how-it-works/

## Coredump

* https://stackoverflow.com/questions/5115613/core-dump-file-analysis

## IPK

* https://raymii.org/s/tutorials/Building_IPK_packages_by_hand.html

## Bash Script

### Bash Script - Give Input to Program Linux

```bash
(
echo
echo
) | ls
```

### Search for Text in Files

```bash
grep -nwr 'path to folder' -e 'text to search' 
```

### Ref.

* https://stackoverflow.com/questions/16956810/how-do-i-find-all-files-containing-specific-text-on-linux

## Search

```bash
grep -rnw '/path/to/somewhere/' -e 'pattern'
```

## xxd

Display binary in hex format.

```bash
xxd -i 
```

### Guidelines

* https://google.github.io/styleguide/shellguide.html

### String Handling

* https://www.delftstack.com/howto/linux/how-to-concatenate-strings-using-bash/#:~:text=String%20concatenation%20is%20one%20of,them%20using%20the%20%2B%3D%20operator.

### Array [@]

* https://stackoverflow.com/questions/64672694/what-does-mean-in-bash

### Bash Script

* https://linuxconfig.org/bash-scripting-tutorial

#### Difference Between Double and Single Quotes

* https://stackoverflow.com/questions/6697753/difference-between-single-and-double-quotes-in-bash
* https://stackoverflow.com/questions/10067266/when-to-wrap-quotes-around-a-shell-variable/42104627#42104627

### Bash Glob

Similar to regex but not regex.

* https://mywiki.wooledge.org/glob

### Bracket If Condition

* https://unix.stackexchange.com/questions/306111/what-is-the-difference-between-the-bash-operators-vs-vs-vs#:~:text=double%20brackets%20are%20an%20alternate,f%20%22%24file%22%20%5D%20.

### Tutorial

* https://devhints.io/bash

### Regex Operation =~

```bash
=~
```

### String Compare Regex

* https://stackoverflow.com/questions/229551/how-to-check-if-a-string-contains-a-substring-in-bash

## Switch Case

### Double Semicolon

It's part of case syntax.

* https://www.linuxquestions.org/questions/linux-newbie-8/bash-scripting-options-double-semicolon-4175600617/

### Option and Parameter

* https://www.google.com/amp/s/likegeeks.com/linux-bash-scripting-awesome-guide-part3/amp/

### Substring Remove

```bash
srk="This is an example text. This is an example text."
# From beginning
echo "${srk#This}"
echo "${srk##This}"

x=demo.txt
echo ${x#*.}
txt
# From end
x=demo.txt
echo ${x%.*}
demo
```

### Ref.

* https://wiki.bash-hackers.org/syntax/pe#variable_name_expansion

### Parameter Search and Replace

```bash
srk="This is an example text. The time is 10am."
echo ${srk//[0-9]/1}
# This is an example text. The time is 11am.

srk="This is an example text. {()The time is 10am.}"
echo ${srk//[[:punct:]]/1}
# This is an example text1 111The time is 10am11
```

### Ref.

* https://wiki.bash-hackers.org/syntax/pattern
* https://www.regular-expressions.info/posixbrackets.html

## sed

Stream Editor

```bash
echo test | sed 's\test\one\g'
```

```bash
x=$(xxd -l 16 -p /dev/random)
echo 990001${x}
```

```bash
sed "s/xxxx/yyyy" -i input.txt
```

```bash
sed "s/xxxx/${data}" -i input.txt
```

```bash
sed "s/xxxx/$data" -i input.txt
```

Save to output.txt

```bash
sed "s/xxxx/yyyy" input.txt > output.txt
```

## Command to Ignore the HUP (Hangup) Signal

```bash
nohup 
```

### Ref.

* https://linux.101hacks.com/unix/nohup-command/
* https://linuxize.com/post/how-to-run-linux-commands-in-background/

## ifconfig

```bash
ifconfig eth0
```

## CAN Tools

```bash
sudo apt install can-utils
```

### Ref.
1. https://elinux.org/Bringing_CAN_interface_up

## Install libc6

```bash
apt-get upgrade libc6
```

### Ref.
* https://github.com/processone/ejabberd/issues/2650

## Running Commands One After Another

* https://superuser.com/questions/1079403/how-to-run-multiple-commands-one-after-another-in-cmd/1079420
* https://stackoverflow.com/questions/5130847/running-multiple-commands-in-one-line-in-shell

## Cron Job

* Minute
* Hour
* Day of month
* Month
* Week days

2/15 i.e., repeat every 15 minutes, start at 2 minutes.

```bash
* * * * *
```

## sort

```bash
sort -k 2 -numeric input.txt
```

```bash
cat input.txt | grep <filter> | sort -r
```

* https://stackoverflow.com/questions/6438896/sorting-data-based-on-second-column-of-a-file

## Get First Line

### head

-n number of lines to print
-q do not output file header

```bash
head -n 1 -q input.txt
```

## du

To get directory size.

```bash

du -h -d1 /
```

## chown and chmod

## Raspi WiFi USB Dongle Setup

* https://www.muchen.ca/blog/2020/ubuntu-realtek-wifi-setup/

```bash
git clone https://github.com/brektrou/rtl8821CU.git
cd rtl8821CU/
chmod +x dkms-install.sh
sudo ./dkms-install.sh
sudo modprobe 8821cu
```

## Streaming

* https://www.sigmdel.ca/michel/ha/rpi/streaming_en.html

```bash
/usr/local/bin/mjpg_streamer -i "/usr/local/lib/mjpg-streamer/input_uvc.so -n -f 10 -r 1280x720" -o "/usr/local/lib/mjpg-streamer/output_http.so -p 8080 -w /usr/local/share/mjpg-streamer/www"

nohup /usr/local/bin/mjpg_streamer -i "/usr/local/lib/mjpg-streamer/input_uvc.so -n -f 10 -r 1280x720" -o "/usr/local/lib/mjpg-streamer/output_http.so -p 8080 -w /usr/local/share/mjpg-streamer/www"
```

### Autostart Octoprint in Ubuntu Server 

https://homeassistant.jongriffith.com/Tutorials/Octoprint/How-to-install-Octoprint-on-Ubuntu-Server/

## How to Find the Program Location?

```bash
whereis <program name>
whereis ls
```

## Convert Windows Path to Linux

```bash
pth="C:/"
echo "/$pth" | sed 's/\\/\//g' | sed 's/://'
```

* https://stackoverflow.com/questions/13701218/windows-path-to-posix-path-conversion-in-bash

## Linux cd to Previous Directory

```bash
cd -
```

## qwe Bookmark Directory  

```bash
source https://raw.githubusercontent.com/olafurw/qwe/refs/heads/main/qwe.source
qwe -a <directory>
```

## alias 

```bash
alias q=qwe
alias c=clear
```

## Linux File System

> MTD -> UBI Volume -> UBIFS

## Useful 

* https://tldr.inbrowser.app/pages/common/delta

## Useful Programs 

* tldr
* zoxide
* exa
* tmux
* bat
* Delta
* lf
* fzf
* htop
* btop
* neovim
* neofetch
* cmatrix

## Ethernet Interface Naming

* https://stackoverflow.com/questions/54194789/etc-network-interfaces-whats-ethnum-mean

## Linux Expand Partition

* https://forum.cloudron.io/topic/6086/ubuntu-20-04-how-to-extend-partition-for-noobs

## zcat

Linux utility to cat zip file.

## zgrep

grep without unpacking.

```bash
zgrep CONFIG_OPTION /proc/config.gz

/proc/config.gz
/boot/config
/boot/config-$(uname -r)
```

## tree

Command to view directory structure in tree format.

```bash
tree
.
├── hello
│   ├── files
│   │   ├── hello.c
│   │   └── Makefile
│   └── hello_1.0.bb
└── README.md
```

### epoll

Linux non blocking wait to monotor event

### put cursor at the bottom of the screen

```bash
__prompt_to_bottom_line() {
  tput cup $LINES
}
alias clear='clear && __prompt_to_bottom_line'
__prompt_to_bottom_line
```

#### Ref

* https://stackoverflow.com/questions/32618502/is-there-a-way-to-keep-the-terminal-shell-prompt-in-the-middle-top-of-page

### Setting SWAP

Setting `swap` is not possible in `nfs`

### csr gen
#!/bin/bash

# Set the RSA key size (default 2048)
KEY_SIZE=2048
PRIVATE_KEY="device_key.pem"
CSR_FILE="device.csr"

# Get the device serial number (Modify for your system)
DEVICE_SN=$(cat /sys/class/dmi/id/product_serial 2>/dev/null || echo "UNKNOWN_SN")

# Fallback if serial number is unavailable
if [[ -z "$DEVICE_SN" || "$DEVICE_SN" == "UNKNOWN_SN" ]]; then
    echo "Warning: Could not retrieve device serial number. Using default 'UNKNOWN_SN'."
fi

# Define CSR subject (Modify Country, State, etc., as needed)
SUBJECT="/C=US/ST=California/L=San Francisco/O=MyCompany/OU=Devices/CN=$DEVICE_SN"

# Generate the RSA private key
echo "Generating RSA key ($KEY_SIZE bits)..."
openssl genpkey -algorithm RSA -out "$PRIVATE_KEY" -pkeyopt rsa_keygen_bits:$KEY_SIZE

# Generate the CSR with the device serial number in the subject
echo "Creating CSR with subject: $SUBJECT"
openssl req -new -key "$PRIVATE_KEY" -out "$CSR_FILE" -subj "$SUBJECT"

echo "CSR generated: $CSR_FILE"
echo "Private key: $PRIVATE_KEY"

'''

---
#!/bin/bash

# Input TLV binary file
INPUT_FILE="tlv_data.bin"

# Output directory for extracted TLVs
OUTPUT_DIR="tlv_extracted"

# Create output directory if not exists
mkdir -p "$OUTPUT_DIR"

# Read binary data as hex
HEX_DATA=$(xxd -p -c 1000 "$INPUT_FILE" | tr -d '\n')

# Function to convert hex to decimal
hex_to_dec() {
    echo "$((16#$1))"
}

# Parse the TLV data
INDEX=0
while [ $INDEX -lt ${#HEX_DATA} ]; do
    # Extract Tag (1 byte)
    TAG=${HEX_DATA:$INDEX:2}
    INDEX=$((INDEX + 2))

    # Extract Length (1 byte)
    LENGTH_HEX=${HEX_DATA:$INDEX:2}
    INDEX=$((INDEX + 2))

    LENGTH=$(hex_to_dec "$LENGTH_HEX")

    # Extract Value (LENGTH bytes)
    VALUE=${HEX_DATA:$INDEX:$((LENGTH * 2))}
    INDEX=$((INDEX + (LENGTH * 2)))

    # Write the value to a binary file
    OUTPUT_FILE="$OUTPUT_DIR/tag_${TAG}.bin"
    echo -n "$VALUE" | xxd -r -p > "$OUTPUT_FILE"

    echo "Extracted Tag $TAG (Length: $LENGTH) to $OUTPUT_FILE"
done
---

echo "TLV parsing completed."