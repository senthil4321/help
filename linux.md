# Linux
## shell script
### Redirection
`<<<` is not supported by sh.
### Ref.
1. https://unix.stackexchange.com/questions/208911/while-read-loop
1. http://www.compciv.org/topics/bash/variables-and-substitution/#:~:text=From%20the%20Bash%20documentation%3A,with%20any%20trailing%20newlines%20deleted.
### awk
####
#### Ref.
1. https://stackoverflow.com/questions/8748831/when-do-we-need-curly-braces-around-shell-variables
### curl
@ before file\
@- to read from stdin
```

```
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

### CAN Tools
```
sudo apt install can-utils

```
#### Ref.
1. https://elinux.org/Bringing_CAN_interface_up
