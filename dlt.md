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
```
dlt-control -e ECU1 -a LOG -c TEST -s 4096 -x 111212 127.0.0.1
dlt-control 127.0.0.1 -e ECU1 -a LOG -c TEST -s 4096 -m Hello World

dlt-example-user -n 1000 -d 100000 test
```

1. `-x` Send Injection with hex data
1. ` -m` Send Injection with ASCII data 
#### Ref.
1. [Info](https://lists.linuxfoundation.org/pipermail/genivi-diagnostic-log-and-trace/2015-December/000857.html)
***

