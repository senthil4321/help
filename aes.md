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

w0 = 32 bits per word (word size of 32 bits)

w0 w1 w2 w3 = 4 bytes * 4 = 16 bytes (128 bits)

w0 to w43 = 4 * 44 = 176 bytes
16 bytes * 11 rounds= 176 bytes

```
