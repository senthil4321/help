# help file for git commands
## remove last commit 
```
git reset HEAD^
```
## remove all files/folders added
``
git reset HEAD
``

## remove files inside a folder
``
git reset HEAD -- .
``

## git How to display the config?
```shell
git config --list
```
***
## git How to Fix Git Self Signed Certificate in Certificate Chain on Windows?
> self signed certificate in certificate chain \
> unable to get local issuer certificate \
> Opening the `ca-bundle.crt` location and copying the git `xxx.cer` will solve the problem \
> Use the below command to get the cert path 

```shell
git config --list --show-origin
```
### Ref.
* [Fix self-signed cert.](https://mattferderer.com/fix-git-self-signed-certificate-in-certificate-chain-on-windows#:~:text=A%20popular%20workaround%20is%20to,that%20creates%20large%20security%20risks.&text=The%20solution%20is%20to%20add%20the%20certificates%20to%20Git's%20trusted%20certificates.)
***
## tag
```
git tag -a v1.4 -m "my version 1.4"
git tag v1.4-lw

git push origin --tags
git push origin v1.5

git tag
git tag -l "v1.8.5*"

git checkout v2.0.0
```

### tag later
```
git tag -a v1.2 9fceb02
git log --pretty=oneline
```
### Ref.
* https://git-scm.com/book/en/v2/Git-Basics-Tagging
## git ignore
To exclude all the files with .settings in the project
```git
*.settings
*.project
```
## always rebase while pull
```
git config --global pull.rebase true
```
### Ref 
* https://sdqweb.ipd.kit.edu/wiki/Git_pull_--rebase_vs._--merge
