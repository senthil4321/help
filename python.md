# Python Help
###
* python modules are packaged in package
### Python online compiler
* https://www.programiz.com/python-programming/online-compiler/
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
***
### How to install python from github
```bash
sudo python setup.py install
```
#### Ref.
1. https://stackoverflow.com/questions/15268953/how-to-install-python-package-from-github
***
### How to run unit test in python ?
```bash
python3 -m unittest discover -p dlt_client_unit_tests.py 
```
#### Ref.
1.https://stackoverflow.com/questions/1732438/how-do-i-run-all-python-unit-tests-in-a-directory
* * *
### Python Module and Package
> Python Module is a file with python code
Rr
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
#### How to combining array ?
```python
    a = bytearray((0x01, 0x22 , 0x55 ))
    b = bytearray((0x01, 0x02 , 0x03 ))
    print(a+b)
```
#### How to get byte array from hex string?
Example1
```python
x = "42";
print(bytes.fromhex(s))
```
Example2
```python 
data = bytearray.fromhex("1234567890aabbccddeeff")
print(data.hex())
```
#### How to convert string to byte array?
```python
s= "HELLO"
print(str.encode(s))
```
#### How to print byte array in hex string?
> Option1 Best :heart:
```python
a = bytearray((0x01, 0x02 , 0x03 ))
print(a.hex())
```
> Option2
```python
a = bytearray((0x01, 0x02 , 0x03 ))
import binascii
print(binascii.hexlify(a))
```
#### Print type of variable 
```python
data = "1234"
print(type(data))
```
> str
> byte
#### __repr__ and __str__
repr is used for debugging object
str is used for printing object
```python

```
***
#### _ underscore
Underscore is used in variable and method names to denote private
***
#### property object and decoraters
``` python
```
***
### Modules
#### console-menu
* https://pypi.org/project/console-menu/  
#### CAN
* https://pypi.org/project/can-isotp/
* https://python-can.readthedocs.io/en/master/
***
### Python Eclipse
#### How to manage python modules libraries from within eclipse?
>  It is possible to manage python libraries from the eclipse. \
##### Steps
1. Goto Preference > Pydev Interpreters > Python Interpreters
#### How to solve unresolved module issue?
> Add the source folder to the phydev \
> Note: Changes to take affect the file must be closed and reopened
in the editor.
### make sound
```python
import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)
```
### get python architecture
```
import platform
platform.architecture()[0]

```
### Cheatsheet
1. https://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf
* * *
#### Ref.
1. https://medium.com/@butteredwaffles/python-packages-and-modules-explained-part-1-ff304c4f19dd
1. https://stackoverflow.com/questions/419163/what-does-if-name-main-do
1. https://cmdlinetips.com/2014/03/how-to-run-a-shell-command-from-python-and-get-the-output/
1. https://stackoverflow.com/questions/11615455/python-start-new-command-prompt-on-windows-and-wait-for-it-finish-exit
1. https://www.endpoint.com/blog/2015/01/28/getting-realtime-output-using-python
1. https://www.google.com/amp/s/www.geeksforgeeks.org/str-vs-repr-in-python/amp/
1. https://www.programiz.com/python-programming/property
##### Bytearray convertion
* https://stackoverflow.com/questions/7585435/best-way-to-convert-string-to-bytes-in-python-3/7585619
* https://www.w3resource.com/python/python-bytes.php#hex-string-byte
* https://stackoverflow.com/questions/11624190/python-convert-string-to-byte-array
##### How to access command line arguments?
* https://stackoverflow.com/questions/4033723/how-do-i-access-command-line-arguments-in-python
* https://www.tutorialspoint.com/python/python_command_line_arguments.htm
***
This is a guide on Markdown [Markdown][1].
[1]: http://en.wikipedia.org/wiki/Markdown
*** 

### python key press
* https://stackoverflow.com/questions/11918999/key-listeners-in-python

### python beep
* https://stackoverflow.com/questions/6537481/python-making-a-beep-noise

### python virenv
* https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b

## jupyter
  https://stackoverflow.com/questions/52330492/how-to-change-jupyter-notebook-windows-shell-to-bash

### Run Visual Studio in interactive Mode
* https://stackoverflow.com/questions/49992300/python-how-to-show-graph-in-visual-studio-code-itself

### Signal Processing with Python
* https://courses.ideate.cmu.edu/16-223/f2021/text/code/pico-signals.html
---
### Copy Buffer to Another Bugger
``` Python
data1[pos:pos+len(data2)] = data2
data1[0:0+len(data2)] = data2
```
```
size = 10
data1[0:0+len(size)] = data2[0:size]
```
#### Ref.
* https://stackoverflow.com/questions/10633881/how-to-copy-a-python-bytearray-buffer
---
### Python Initialise byte array with value 
```
initValue = 2
size = 1024
bytearray(size)
bytearray([initValue] * size)
```
```
bytearray(50)
bytearray([1] * 50)

```
#### Ref.
* https://stackoverflow.com/questions/9184489/how-to-create-a-bytes-or-bytearray-of-given-length-filled-with-zeros-in-python

## Encryption 
```python
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

def encrypt(plaintext, key):
    # Generate a random IV (Initialization Vector)
    iv = os.urandom(16)

    # Create a Cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    # Create an encryptor
    encryptor = cipher.encryptor()

    # Pad the plaintext to be compatible with the block size
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()

    # Encrypt the padded plaintext
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

    return iv + ciphertext

def main():
    # Example plaintext
    plaintext = b"Secret message that needs to be encrypted"

    # 256-bit key (32 bytes)
    key = os.urandom(32)

    # Encrypt the plaintext
    ciphertext = encrypt(plaintext, key)

    print(f"Ciphertext: {ciphertext}")

if __name__ == "__main__":
    main()
```
### f-string
### f-string and self documenting expression 
```
print(f'{theta=}  {cos(radians(theta))=:.3f}')
theta=30  cos(radians(theta))=0.866
```
### format-specification-mini-language
```
'{:<30}'.format('left aligned')
'left aligned                  '
```
```
for align, text in zip('<^>', ['left', 'center', 'right']):
    '{0:{fill}{align}16}'.format(text, fill=align, align=align)
```
* https://docs.python.org/3/library/string.html#format-specification-mini-language
### zip command in for loop
> zip allows you to iterate two lists at the same time, so, for example, the following code
```
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]

for letter, number in zip(letters, numbers):
    print(f'{letter} -> {number}')
```
> Passing Arguments of Unequal Length - shorted list is taken
> Strict mode - > throws error - zip(range(5), range(100), strict=True)
* https://stackoverflow.com/questions/49783594/for-loop-and-zip-in-python
* https://realpython.com/python-zip-function/
