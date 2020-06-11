# Python Help
###
1. python modules are packaged in package

### Python anaconda
is a distribution framework.

### setup.py and requirement.txt
#### requirement.txt
helps you to set up your development environment
```
pip install -r requirements.txt
```
#### setup.py 
allows you to create packages that you can redistribute

https://stackoverflow.com/questions/43658870/requirements-txt-vs-setup-py
### How to install python from github
`
sudo python setup.py install
`
#### Ref.
1. https://stackoverflow.com/questions/15268953/how-to-install-python-package-from-github
***
### How to run unit test in python ?
```
python3 -m unittest discover -p dlt_client_unit_tests.py 
```
___
#### Ref.
1.https://stackoverflow.com/questions/1732438/how-do-i-run-all-python-unit-tests-in-a-directory

### Libraries
#### console-menu
1.https://pypi.org/project/console-menu/  

### cheatsheet
1. https://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf

### Python Module and Package
> Python Module is a file with python code

> Python Package is collection of python Modules
#### Module
1. If module has `if __name__=="main"`, then the code is executed.
   This happens when the file is directly executed.
### Code snippet
```python
out = subprocess.Popen('dir',shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT )
    stdout,stderr = out.communicate()

input("Press Enter to continue...") 

import DEMO as DEMO

convert bytes to string 
.decode("utf-8") 

if title_search:
    title = title_search.group(0)
```
#### Ref.
1. https://medium.com/@butteredwaffles/python-packages-and-modules-explained-part-1-ff304c4f19dd
1. https://stackoverflow.com/questions/419163/what-does-if-name-main-do
1. https://cmdlinetips.com/2014/03/how-to-run-a-shell-command-from-python-and-get-the-output/
1. https://stackoverflow.com/questions/11615455/python-start-new-command-prompt-on-windows-and-wait-for-it-finish-exit
This is a guide on Markdown [Markdown][1].

[1]: http://en.wikipedia.org/wiki/Markdown

