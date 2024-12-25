# Linux Basics

## Log Handling

* `journald` has replaced syslog.
* `dmesg` to read kernel ring buffer`
* `syslog` mechanism for general system logs used by applicaitons

### Redirecting Startup Script Logs to Syslog

```bash
exec 1> >(logger -s -t $(basename $0)) 2>&1
```

#### Ref

1. https://www.urbanautomaton.com/blog/2014/09/09/redirecting-bash-script-output-to-syslog/
1. https://serverfault.com/questions/341919/how-to-find-error-messages-from-linux-init-d-rc-d-scripts