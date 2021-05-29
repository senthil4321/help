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
```
od -x 
```
#### Ref.
[Manpage](https://man7.org/linux/man-pages/man1/od.1.html)

---
### awk
### Variable and string
#### when we-need-curly-braces-around-shell-variables
#### Ref.
1. https://stackoverflow.com/questions/8748831/when-do-we-need-curly-braces-around-shell-variables
#### Parameter Expansion
* https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html

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
### passing password to scp ssh
> Switch to key based authentication
```
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
```
sudo fdisk -l
sudo mount -o remount,rw /dev/sdc1
```
---
## top
> Program to get cpu and memory usage
```
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
Please the below line in the .bash_rc
```
export PROMPT_COMMAND='history -a'
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
## Ref.
1. https://unix.stackexchange.com/questions/145250/where-is-bashs-history-stored
1. https://askubuntu.com/questions/391082/how-to-see-time-stamps-in-bash-history

***
### command to ignore the HUP (hangup) signal
```bash
nohup 
```
Ref.
https://linux.101hacks.com/unix/nohup-command/
running linux command in background
https://linuxize.com/post/how-to-run-linux-commands-in-background/
***
### logs
> `journald` has replaced syslog
#### redirecting startup script logs to syslogs
```bash
exec 1> >(logger -s -t $(basename $0)) 2>&1
```
1. https://www.urbanautomaton.com/blog/2014/09/09/redirecting-bash-script-output-to-syslog/
1. https://serverfault.com/questions/341919/how-to-find-error-messages-from-linux-init-d-rc-d-scripts
***
### ifconfig
'''
ifconfig eth0
'''
### CAN Tools
```
sudo apt install can-utils

```
#### Ref.
1. https://elinux.org/Bringing_CAN_interface_up

### install libc6
```
apt-get upgrade libc6
```
#### Ref.
* https://github.com/processone/ejabberd/issues/2650
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
## bash script- give input to program linux 
```bash
(
echo
echo
) | ls
```
## Secure boot
* https://elinux.org/images/e/e0/Josserand-schulz-secure-boot.pdf
## coredump
* https://stackoverflow.com/questions/5115613/core-dump-file-analysis
## ipk
* https://raymii.org/s/tutorials/Building_IPK_packages_by_hand.html
## search for text in files
'''bash
grep -nwr 'path' -e 'test' 
'''
### Ref.
* https://stackoverflow.com/questions/16956810/how-do-i-find-all-files-containing-specific-text-on-linux
## search
```
grep -rnw '/path/to/somewhere/' -e 'pattern'
```
### xxd
Display binary in hex Format
```
xxd -i 
```
### overlay fs
```bash
mount -t overlay overlay -o lowerdir=/usr/bin,upperdir=/mnt/mmc/usr/bin_upper,workdir=/mnt/mmc/wordir /usr/bin
```
* https://www.datalight.com/blog/2016/01/27/explaining-overlayfs-%E2%80%93-what-it-does-and-how-it-works/
### running cmd one after another
* https://superuser.com/questions/1079403/how-to-run-multiple-commands-one-after-another-in-cmd/1079420
* https://stackoverflow.com/questions/5130847/running-multiple-commands-in-one-line-in-shell

### guidelines
* https://google.github.io/styleguide/shellguide.html

### string handling

* https://www.delftstack.com/howto/linux/how-to-concatenate-strings-using-bash/#:~:text=String%20concatenation%20is%20one%20of,them%20using%20the%20%2B%3D%20operator.

### array [@]
* https://stackoverflow.com/questions/64672694/what-does-mean-in-bash

### bash script
* https://linuxconfig.org/bash-scripting-tutorial

#### todo
* https://stackoverflow.com/questions/6697753/difference-between-single-and-double-quotes-in-bash
* https://stackoverflow.com/questions/10067266/when-to-wrap-quotes-around-a-shell-variable/42104627#42104627
### bash glob
Similar to regex but not regex
* https://mywiki.wooledge.org/glob
