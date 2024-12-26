# Linux Basics

## Log Handling

* `journald` has replaced syslog.
* `dmesg` to read kernel ring buffer
* `syslog` mechanism for general system logs used by applicaitons

### Redirecting Startup Script Logs to Syslog

```bash
exec 1> >(logger -s -t $(basename $0)) 2>&1
```

#### Ref

1. https://www.urbanautomaton.com/blog/2014/09/09/redirecting-bash-script-output-to-syslog/
1. https://serverfault.com/questions/341919/how-to-find-error-messages-from-linux-init-d-rc-d-scripts

## systemd

```bash
systemd-analyze
systemd-analyze blame
systemd-analyze critical-chain
systemd-analyze plot > boot_sequence.svg
```
## How to know if linux system is finished booting?

```bash
systemctl is-active multi-user.target
```
## Linux Device Mapper

The Linux Device Mapper is a framework provided by the Linux kernel for mapping physical block devices onto higher-level virtual block devices.

## LUKS

LUKS (Linux Unified Key Setup) is a standard for disk encryption in Linux.

## Kernel Module Signing

Kernel Module is signed with private key during build time and verified during loading by the Kernel. The Kernel Module Verification key can be compiled into the Kernel.

## How to get program library depedency ?

``` bash
ldd srk-socket-server
```
## How to get depedency tree of c program?

```bash
gcc -M socket_server.c
```
