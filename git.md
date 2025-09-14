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
* [Fix self-signed cert.](https://mattferderer.com/fix-git-self-signed-certificate-in-certificate-chain-on-windows#:~:text=A%20popular%20workaround%20is%20to,that%20creates%20large%20security%20risks.[...]
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
## always rebase while pull ❤️
```
git config --global pull.rebase true
```
### Ref 
* https://sdqweb.ipd.kit.edu/wiki/Git_pull_--rebase_vs._--merge

## git staging
* https://stackoverflow.com/questions/19730565/how-to-remove-files-from-git-staging-area

## git difftool 
it is possible to configure beyond compare as diff tool
it is possible to view differences in whole folder

***

## git rebase vs git merge

### git merge (used in master branch)

Merges changes from another branch into the current branch, creating a merge commit if there are changes. Commonly used to integrate feature branches into the master branch.

```shell
git checkout master
git merge feature-branch
```
- Preserves the history of all branches.
- Creates a merge commit.
- Useful for combining finished features into master.

### git rebase (used in feature branch)

Reapplies commits from your current branch onto another branch, creating a linear history. Commonly used to keep feature branches up-to-date with master before merging.

```shell
git checkout feature-branch
git rebase master
```
- Rewrites commit history for a cleaner, linear history.
- No merge commits.
- Useful to update your feature branch with latest master changes.

#### Typical workflow:
1. Work on `feature-branch`.
2. Periodically rebase onto updated master:
   ```
   git fetch origin
   git rebase origin/master
   ```
3. Resolve any conflicts, continue with:
   ```
   git rebase --continue
   ```
4. Merge feature branch into master (using merge).

### References
- [git merge](https://git-scm.com/docs/git-merge)
- [git rebase](https://git-scm.com/docs/git-rebase)
- [Atlassian: Git Merge vs Rebase](https://www.atlassian.com/git/tutorials/merging-vs-rebasing)
