# scp
## putty scp
* http://the.earth.li/~sgtatham/putty/0.52/htmldoc/Chapter5.html
* https://stackoverflow.com/questions/23080097/command-to-automatically-input-password-for-pscp

### pscp
Use this tool to copy file from/to target
```sh
pscp -2 -scp -pw xxxx xxxx.txt root@192.168.0.5:/data
```
### plink
```sh
plink root@192.168.0.5 -2 -ssh ls /data/ -pw xxxx
```
#### Diff between scp and sftp
> Jenkins scp plugin uses sftp. This might not be supported in all embedded targets.
### diable prompt
* https://stackoverflow.com/questions/7638741/automatically-accept-rsa-fingerprint-using-pscp
```bat
echo y | pscp ""
```
