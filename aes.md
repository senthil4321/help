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

## Binary Addition and Multiplication

* Binary Multiplication

* Parity Addition - XOR
    * there is never a carry
``` c
        if (hi_bit_set) {
            a ^= 0x1B; /* x^8 + x^4 + x^3 + x + 1 */
        }
```

### Ref
* https://crypto.stackexchange.com/questions/2402/how-to-solve-mixcolumns
* https://web.math.princeton.edu/math_alive/Crypto/Lab1/ParAdd.html
* https://en.wikipedia.org/wiki/Rijndael_MixColumns
* https://en.wikipedia.org/wiki/Talk:Rijndael_MixColumns

## Other
* https://www.youtube.com/watch?v=w4aWIVhcUyo&t=22s
* https://braincoke.fr/blog/2020/08/the-aes-key-schedule-explained/#aes-in-summary

## AES CCM
Combination of AES CTR and CBC
* CTR for Encryption
* CBC without IV for MAC
