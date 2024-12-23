# Linux
## shell script
### Redirection
`<<<` is not supported by sh.
### Ref.
1. https://unix.stackexchange.com/questions/208911/while-read-loop
1. [Link2](http://www.compciv.org/topics/bash/variables-and-substitution/#:~:text=From%20the%20Bash%20documentation%3A,with%20any%20trailing%20newlines%20deleted.)
### od 
>> Print file in hex and other formats
>> With no FILE, or when FILE is -, read standard input

>> RADIX is d for decimal, o for octal, x for hexadecimal or n for none
```bash
od -x 
```
#### Ref.
[Manpage](https://man7.org/linux/man-pages/man1/od.1.html)

---
### awk
---
### Variable and string
---
#### when we-need-curly-braces-around-shell-variables
#### Ref.
1. https://stackoverflow.com/questions/8748831/when-do-we-need-curly-braces-around-shell-variables
#### Parameter Expansion
* https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html
* https://wiki.bash-hackers.org/syntax/pe
### variable parameter
A parameter is an entity that stores values
### globbing file expansion
Bash does carry out filename expansion
 [1] -- a process known as globbing 
-- but this does not use the standard RE set. 
Instead, globbing recognizes and expands wild cards. 
Globbing interprets the standard wild card characters
 [2] -- * and ?, character lists in square brackets, and certain other special characters (such as ^ for negating the sense of a match).
* https://tldp.org/LDP/abs/html/globbingref.html
---
### shell redirection
* https://unix.stackexchange.com/questions/159513/what-are-the-shells-control-and-redirection-operators
---
### curl
> curl is also available in windows

`@ `before file\
`@- `to read from stdin

Use
`-u `  option to pass username and password \
`-C - ` option to skip already downloaded info

```
```
#### Ref.
* https://stackoverflow.com/questions/11856351/how-to-skip-already-existing-files-when-downloading-with-curl
***
### Change hostname of linux system
Edit the below file to update the hostname of linux system
```bash
/etc/hostname
```
### passing password to scp ssh
> Switch to key based authentication
```bash
sshpass -p "password" scp -r user@example
sudo apt-get install sshpass
sshpass -p password ssh user@hostname
```
***
### dmesg
prints the message buffer of the kernel
Contains message from device driver
***
### udev
**udev** Linux subsystem to handle device event. It enables to trigger script when a device is plugged in.
***
#### Ref.
1. https://stackoverflow.com/questions/7172784/how-do-i-post-json-data-with-curl
1. https://stackoverflow.com/questions/12583930/use-pipe-for-curl-data
## remount read write
```bash
sudo fdisk -l
sudo mount -o remount,rw /dev/sdc1
```
---
## top
> Program to get cpu and memory usage
```bash
top 
```
---
## History
### Enable unlimited command history
```
HISTSIZE=-1 
HISTFILESIZE=-1
```
### Enable imediate history saving
Please the below line in the ~/.bash_rc | ~/.bashrc 
```
export PROMPT_COMMAND='history -a'
```

### Search long commands in history
```
CTRL + R
```
### history run with command number
```
!550 runs the command with number 550. use 'hisotry' to get the number
!-2 
```
### SCP
#### copy from remote pc
```bash
scp username@192.168.0.172:/remote/file.txt ./
```
#### Ref.
* https://my.esecuredata.com/index.php?/knowledgebase/article/21/copying-multiple-files-at-the-same-time-using-scp
## Linux shell commands redirection to multiple place
```bash
echo "SRK fdisk complete" | tee /dev/kmsg | tee /dev/ttyHSL0
```
---
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
### Command to update the config.
```bash
sudo netplan --debug try
sudo netplan --debug generate 
sudo netplan --debug apply
```
### Ref.
1. https://raspberrypi.stackexchange.com/questions/98598/how-to-setup-the-raspberry-pi-3-onboard-wifi-for-ubuntu-server-18-04-with-netpla
### Enable time information in history
```
echo 'HISTTIMEFORMAT="%d/%m/%y %T "' >> ~/.bashrc 
source ~/.bashrc
```
#### Ref.
1. https://unix.stackexchange.com/questions/145250/where-is-bashs-history-stored
1. https://askubuntu.com/questions/391082/how-to-see-time-stamps-in-bash-history

***
## dm verity
### Preparing block device
```bash
dd if=/dev/zero of=./diskimage bs=1M count=10
dd if=/dev/zero of=./dm-hash bs=1M count=10

sudo mount -o loop=/dev/loop17 ./diskimage /mnt/dm-srk-img/
sudo touch /mnt/dm-srk-img/hello.txt
sudo umount /mnt/dm-srk-img/
sudo losetup /dev/loop17 ./dm-hash
sudo losetup /dev/loop18 ./diskimage
```
### Mounting and checking verity
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

## Secure boot
* https://elinux.org/images/e/e0/Josserand-schulz-secure-boot.pdf
## overlay fs
```bash
mount -t overlay overlay -o lowerdir=/usr/bin,upperdir=/mnt/mmc/usr/bin_upper,workdir=/mnt/mmc/wordir /usr/bin
```
* https://www.datalight.com/blog/2016/01/27/explaining-overlayfs-%E2%80%93-what-it-does-and-how-it-works/
---
## coredump
* https://stackoverflow.com/questions/5115613/core-dump-file-analysis
## ipk
* https://raymii.org/s/tutorials/Building_IPK_packages_by_hand.html
---
## Bash Script
### bash script- give input to program linux 
```bash
(
echo
echo
) | ls
```
### search for text in files
```bash
grep -nwr 'path to folder' -e 'text to search' 
```
#### Ref.
* https://stackoverflow.com/questions/16956810/how-do-i-find-all-files-containing-specific-text-on-linux
## search
```bash
grep -rnw '/path/to/somewhere/' -e 'pattern'
```
## xxd
Display binary in hex Format
```bash
xxd -i 
```
---

### guidelines
* https://google.github.io/styleguide/shellguide.html

### string handling
* https://www.delftstack.com/howto/linux/how-to-concatenate-strings-using-bash/#:~:text=String%20concatenation%20is%20one%20of,them%20using%20the%20%2B%3D%20operator.

### array [@]
* https://stackoverflow.com/questions/64672694/what-does-mean-in-bash

### bash script
* https://linuxconfig.org/bash-scripting-tutorial

#### Difference between double and single quotes
* https://stackoverflow.com/questions/6697753/difference-between-single-and-double-quotes-in-bash
* https://stackoverflow.com/questions/10067266/when-to-wrap-quotes-around-a-shell-variable/42104627#42104627
### bash glob
Similar to regex but not regex
* https://mywiki.wooledge.org/glob

---
### Bracket if condition
* https://unix.stackexchange.com/questions/306111/what-is-the-difference-between-the-bash-operators-vs-vs-vs#:~:text=double%20brackets%20are%20an%20alternate,f%20%22%24file%22%20%5D%20.
### tutorial
* https://devhints.io/bash
### Regex operation =~
```bash
=~
```
### string compare regex
* https://stackoverflow.com/questions/229551/how-to-check-if-a-string-contains-a-substring-in-bash
## switch case
### double semicolon
Its part of case syntax

* https://www.linuxquestions.org/questions/linux-newbie-8/bash-scripting-options-double-semicolon-4175600617/
### option and parameter
* https://www.google.com/amp/s/likegeeks.com/linux-bash-scripting-awesome-guide-part3/amp/
---
### substring remove
```bash
srk="This is an example text. This is an example text."
#From begining
echo "${srk#This}"
echo "${srk##This}"

x=demo.txt
echo ${x#*.}
txt
#From end
x=demo.txt
echo ${x%.*}
demo
```
#### Ref.
* https://wiki.bash-hackers.org/syntax/pe#variable_name_expansion
### Paramter search and replace
```bash
srk="This is an example text. The time is 10am."
echo ${srk//[0-9]/1}
#This is an example text. The time is 11am.

srk="This is an example text. {()The time is 10am.}"
echo ${srk//[[:punct:]]/1}
#This is an example text1 111The time is 10am11

```
#### Ref.
* https://wiki.bash-hackers.org/syntax/pattern
* https://www.regular-expressions.info/posixbrackets.html
---
### sed
Stream Editor
```bash
echo test| sed 's\test\one\g'
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
---
### command to ignore the HUP (hangup) signal
```bash
nohup 
```
#### Ref.
* https://linux.101hacks.com/unix/nohup-command/
running linux command in background
* https://linuxize.com/post/how-to-run-linux-commands-in-background/

### logs
> `journald` has replaced syslog
#### redirecting startup script logs to syslogs
```bash
exec 1> >(logger -s -t $(basename $0)) 2>&1
```
#### Ref.
1. https://www.urbanautomaton.com/blog/2014/09/09/redirecting-bash-script-output-to-syslog/
1. https://serverfault.com/questions/341919/how-to-find-error-messages-from-linux-init-d-rc-d-scripts

### ifconfig
```bash
ifconfig eth0
```
### CAN Tools
```bash
sudo apt install can-utils
```
#### Ref.
1. https://elinux.org/Bringing_CAN_interface_up

### install libc6
```bash
apt-get upgrade libc6
```
#### Ref.
* https://github.com/processone/ejabberd/issues/2650
### running cmd one after another
* https://superuser.com/questions/1079403/how-to-run-multiple-commands-one-after-another-in-cmd/1079420
* https://stackoverflow.com/questions/5130847/running-multiple-commands-in-one-line-in-shell
### corn job
* Minute
* Hour
* Day of month
* Month
* Week days

2/15 i.e repeat every 15 minute, start at 2 min

```bash
* * * * *
```
### sort
```bash
sort -k 2 -numeric input.txt
```
```bash
cat input.txt | grep <filter> | sort - r
```
* https://stackoverflow.com/questions/6438896/sorting-data-based-on-second-column-of-a-file
### get first line
#### head
-n no of line to print
-q do not output file header
``` bash
head -n 1 -q input.txt
```
### du
To get directory size
```bash
du -h -d1 /
```
## chown and chmod

### Raspi wifi usb dongle setup
* https://www.muchen.ca/blog/2020/ubuntu-realtek-wifi-setup/
```
git clone https://github.com/brektrou/rtl8821CU.git
cd rtl8821CU/
chmod +x dkms-install.sh
sudo ./dkms-install.sh
sudo modprobe 8821cu
```
### Streaming
* https://www.sigmdel.ca/michel/ha/rpi/streaming_en.html
```
/usr/local/bin/mjpg_streamer -i "/usr/local/lib/mjpg-streamer/input_uvc.so -n -f 10 -r 1280x720" -o "/usr/local/lib/mjpg-streamer/output_http.so -p 8080 -w /usr/local/share/mjpg-streamer/www"

nohup /usr/local/bin/mjpg_streamer -i "/usr/local/lib/mjpg-streamer/input_uvc.so -n -f 10 -r 1280x720" -o "/usr/local/lib/mjpg-streamer/output_http.so -p 8080 -w /usr/local/share/mjpg-streamer/www"

```
#### Autostart octoprint in ubuntu server 
https://homeassistant.jongriffith.com/Tutorials/Octoprint/How-to-install-Octoprint-on-Ubuntu-Server/

### How to find the program location ?
```
whereis <program name>
whereis ls
```
### Convert Windows path to linux
```
pth="C:/"
echo "/$pth" | sed 's/\\/\//g' | sed 's/://'
```
* https://stackoverflow.com/questions/13701218/windows-path-to-posix-path-conversion-in-bash

--- --- ---
### Linux cd to previous directory
```
cd --
```
### qwe Bookmark directory  
```
source https://raw.githubusercontent.com/olafurw/qwe/refs/heads/main/qwe.source
qwe -a <directory>
```
### alias 
```
alias q=qwe
alias c=clear
```
### Linux File System
> MTD ->  UBI Volume -> UBIFS
--- --- ---
### useful 
* https://tldr.inbrowser.app/pages/common/delta
### Useful programs 
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

### Ethernet interface naming
* https://stackoverflow.com/questions/54194789/etc-network-interfaces-whats-ethnum-mean

### Linnux Expand Partition
* https://forum.cloudron.io/topic/6086/ubuntu-20-04-how-to-extend-partition-for-noobs
### zcat
> Linux utility to cat zip file
### zgrep
> grep without unpack
```
zgrep CONFIG_OPTION /proc/config.gz

/proc/config.gz
/boot/config
/boot/config-$(uname -r)
```
### tree
> command to view directory structure in tree format
```
tree
.
├── hello
│   ├── files
│   │   ├── hello.c
│   │   └── Makefile
│   └── hello_1.0.bb
└── README.md

```
---
## vi
### To set Arrow Keys in Edit Mode
```
vi ~/.exrc
set nocompatible
```
#### TODO Read Shortcut
* https://askubuntu.com/questions/353911/hitting-arrow-keys-adds-characters-in-vi-editor
* https://www.cs.colostate.edu/helpdocs/vi.html

#### Shortcut

```text
:xReturn quit vi, writing out modified file to file named in original invocation
:wqReturn quit vi, writing out modified file to file named in original invocation
:qReturn quit (or exit) vi
:q!Return quit vi even though latest changes have not been saved for this vi call

↓ move cursor down one line
↓ move cursor up one line
← move cursor left one character
→ move cursor right one character

u undo whatever you just did; a simple toggle
. redo whatever you just did

i insert text before cursor, until Esc hit
I insert text at beginning of current line, until Esc hit
a append text after cursor, until Esc hit
A append text to end of current line, until Esc hit
o open and put text in a new line below current line, until Esc hit
O open and put text in a new line above current line, until Esc hit

r replace single character under cursor (no Esc needed)
cw change the current word with new text,starting with the character under cursor, until Esc hit
x delete single character under cursor
Nx delete N characters, starting with character under cursor
dw delete the single word beginning with character under cursor
C change (replace) the characters in the current line, until Esc hit
D delete the remainder of the line, starting with current cursor position

dd delete entire current line
Ndd delete N lines, beginning with the current line; e.g., 5dd deletes 5 lines
yy copy (yank, cut) the current line into the buffer
Nyy copy (yank, cut) the next N lines, including the current line, into the buffer
p paste the line(s) in the buffer into the text after the current line

0 (zero) move cursor to start of current line (the one with the cursor)
$ move cursor to end of current line
w move cursor to beginning of next word
b move cursor back to beginning of preceding word
:0Return or 1G move cursor to first line in file
:nReturn or nG move cursor to line n
:$Return or G move cursor to last line in file

/string search forward for occurrence of string in text
?string search backward for occurrence of string in text
n move to next occurrence of search string
N move to next occurrence of search string in opposite directio

```
### epoll
Linux non blocking wait to monotor event

### put cursor at the bottom of the screen
```
__prompt_to_bottom_line() {
  tput cup $LINES
}
alias clear='clear && __prompt_to_bottom_line'
__prompt_to_bottom_line
```
#### Ref
* https://stackoverflow.com/questions/32618502/is-there-a-way-to-keep-the-terminal-shell-prompt-in-the-middle-top-of-page

