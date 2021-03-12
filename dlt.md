# Help for commonly used dlt commands
### How to start dlt-daemon ?
```sh
dlt-daemon
```
***
### dlt-receive with filter
Dltfilter can be created with dlt-viewer gui application.
[dlt-receive][DLT-RECEIVE-SRC]
```
dlt-receive 127.0.0.1 -a -f ../srk-python-dlt/filter/helloxml
```
[helloxml](https://raw.githubusercontent.com/senthil4321/srk-python-dlt/master/filter/helloxml) 

[DLT-RECEIVE-SRC]: https://raw.githubusercontent.com/GENIVI/dlt-daemon/master/src/console/dlt-receive.c "dlt-receive-src"
***
### dlt-control
Control message can be sent both in hex and ASCII
```
dlt-control -e ECU1 -a LOG -c TEST -s 4096 -x '11 12 12' 127.0.0.1
dlt-control -e ECU1 -a LOG -c TEST -s 4096 -m Hello World 127.0.0.1

dlt-example-user -n 1000 -d 100000 test
```

1. `-x` Send Injection with hex data
1. ` -m` Send Injection with ASCII data 
1. `-a` application id, `-c` context id, `-s` service id.
1. host ip address should be passed at the end of the argument list.
1. `dlt-example-user` must be running for the injection to work.
#### Ref.
1. [Info](https://lists.linuxfoundation.org/pipermail/genivi-diagnostic-log-and-trace/2015-December/000857.html)
***
### dlt-adaptor-stdin
Program to send dlt logs from stdin.
```
```
## dlt protocol
### non verbose
* https://github.com/GENIVI/dlt-viewer/blob/master/plugin/nonverboseplugin/nonverboseplugin.cpp
***
### trace
> Trace is used for instrumentation ie. code coverage etc
### Log Analysis
1. https://www.systemticks.de/2019/03/13/analyzing_huge_dlt_log_files_with_elastic_stack.html
