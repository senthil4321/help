# AES
## AES Terminology
* Key Schedule
  
### AES 128
* Nb = 4; // AES standard (4*32) = 128 bits
* Nr = 10;
* Nk = 4;

```
Key Schedule
Number of rounds  = 1 + 10 = 11

K Key size is 16 bytes

w0 = K[0] + K[1] + K[2] + K[3]
 
w0 = 32 bits per word (word size of 32 bits)

w0 w1 w2 w3 = 4 bytes * 4 = 16 bytes (128 bits)

w0 to w43 = 4 * 44 = 176 bytes
16 bytes * 11 rounds= 176 bytes

```

1. rotWord
2. subWord
3. rConWord
   
       subWord xor rConConstant

### Ref
Binary Multiplication
Parity Addition - XOR
  there is never a carry
  

```
```
* https://crypto.stackexchange.com/questions/2402/how-to-solve-mixcolumns
* https://web.math.princeton.edu/math_alive/Crypto/Lab1/ParAdd.html
