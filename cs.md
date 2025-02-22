## tz
* https://blog.quarkslab.com/introduction-to-trusted-execution-environment-arms-trustzone.html
* https://prateekvjoshi.com/2015/02/07/why-are-they-called-elliptic-curves/

---

## algorithms

### Math

### co-prime
> Co-prime numbers are pairs of numbers that do not have any common factor other than 1. There should be a minimum of two numbers to form a set of co-prime numbers. Such numbers have only 1 as their highest common factor, for example, (4 and 7), (5, 7, 9) are co-prime numbers

---

### prime and co-prime
> A prime number is a number that has exactly two factors, 1 and the number itself. For example, 2, 3, 7, 11 and so on are prime numbers. Co-prime numbers are pairs of numbers whose HCF (Highest Common Factor) is 1. For example, (4,9) are co-primes because their only common factor is 1.

1. http://www.cs.sjsu.edu/~stamp/CS265/SecurityEngineering/chapter5_SE/RSAmath.html

---

> In number theory, two integers a and b are coprime, relatively prime or mutually prime if the only positive integer that is a divisor of both of them is 1.[1] Consequently, any prime number that divides a does not divide b, and vice versa. This is equivalent to their greatest common divisor (GCD) being 1.[2] One says also a is prime to b or a is coprime with b.

> The numbers 8 and 9 are coprime, despite the fact that neither considered individually is a prime number, since 1 is their only common divisor. On the other hand, 6 and 9 are not coprime, because they are both divisible by 3.

### are prime numbers coprime
> For example: (11, 13) Here, 11 and 13 are coprime numbers, and their LCM is 11 × 13 = 143. Because prime numbers only share one common factor, 1, any two prime numbers are always coprime.

#### References
* https://en.m.wikipedia.org/wiki/Coprime_integers

---

## ec

Number of points in the elliptic curve over finite field is called order of elliptic curve. 
Total number of points is called order. 

Cofactor of 1 means only one sub group.

1. https://cryptobook.nakov.com/digital-signatures/eddsa-and-ed25519
1. https://en.m.wikipedia.org/wiki/Barrett_reduction
1. https://github.com/rweather/arduinolibs/blob/master/libraries/Crypto/Ed25519.cpp#L304
1. https://en.m.wikipedia.org/wiki/Extended_Euclidean_algorithm
1. algebraic curves over finite fields
1. https://www.allaboutcircuits.com/technical-articles/elliptic-curve-cryptography-in-embedded-systems/
1. https://cryptobook.nakov.com/asymmetric-key-ciphers/elliptic-curve-cryptography-ecc
1. https://medium.com/asecuritysite-when-bob-met-alice/so-what-have-prime-numbers-and-galois-fields-to-do-with-your-privacy-2dff9881361e

### start here

1. https://andrea.corbellini.name/2015/05/23/elliptic-curve-cryptography-finite-fields-and-discrete-logarithms/
1. https://andrea.corbellini.name/2015/05/17/elliptic-curve-cryptography-a-gentle-introduction/

### ec
1. https://fission.codes/blog/everything-you-wanted-to-know-about-elliptic-curve-cryptography/
1. https://graui.de/code/elliptic2/
1. https://asecuritysite.com/curve25519/eddsa
1. https://asecuritysite.com/curve25519
1. https://github.com/nakov/Practical-Cryptography-for-Developers-Book/blob/master/asymmetric-key-ciphers/elliptic-curve-cryptography-ecc.md
   
#### Elliptic curve Point Addition online

1. https://andrea.corbellini.name/ecc/interactive/modk-add.html

#### Finite Field

> A finite field is, first of all, a set with a finite number of elements. An example of finite field is the set of integers modulo p, where `p` is a prime number.

> Find the multiplicative inverse of a number and then perform a single multiplication.

Computing the multiplicative inverse can be “easily” done with the extended Euclidean algorithm.

### tool

1. https://www.dcode.fr/modular-inverse

---

## rsa

> For a positive integer n, define φ(n) to be the number of integers less than n that are relatively prime with n. For example, φ(12) = 4, since only 11, 7, 5 and 1 are less than 12 and relatively prime to 12, while φ(7) = 6. In fact, for any prime number p we have φ(p) = p - 1.

1. https://www.cantorsparadise.com/rsa-algorithm-in-depth-mathematical-walk-through-3bf33759022a
1. https://www.di-mgt.com.au/rsa_alg.html#simpleexample
1. https://doctrina.org/How-RSA-Works-With-Examples.html
1. https://cryptobook.nakov.com/asymmetric-key-ciphers/the-rsa-cryptosystem-concepts
1. https://doctrina.org/How-RSA-Works-With-Examples.html#

### RSA Arithmetic

```
The encryption of m = 2 is c = 2^7 mod 33 = 29
The decryption of c = 29 is m = 29^3 mod 33 = 2
```

#### References
* https://www.cs.utexas.edu/users/mitra/honors/soln.html

---

### multiplicative inverse 
> A multiplicative inverse for x is a number that when multiplied by x, will equal 1. The multiplicative inverse of x is written as x−1 and is defined as so:

x⋅x−1=1
The greatest common divisor (gcd) between two numbers is the largest integer that will divide both numbers. For example, gcd(4,10)=2.

The interesting thing is that if two numbers have a gcd of 1, then the smaller of the two numbers has a multiplicative inverse in the modulo of the larger number. It is expressed in the following equation.

### chacha20
ChaCha20 is a stream cipher.

### md2 md4 md5 md6
> Message digest algorithm

### SM2
SM2 is actually an elliptic curve based algorithm.
SM2 has both signature and encryption scheme.

### SM3
ShangMi 3 (SM3) is a cryptographic hash function.

### SM4
SM4 is a block cipher.

### sha256
SHA-256 is a hash algorithm.

## online tool
* https://cyberchef.io/

## AES Implementation
* AES 128 Implementation

---

## IPSec
```
sudo apt install strongswan strongswan-pki libcharon-extra-plugins libstrongswan-extra-plugins
sudo apt-get install charon-systemd
```
```
sudo ipsec statusall
sudo swanctl --log --raw
sudo swanctl --log --pretty
sudo swanctl --reload-settings 

sudo systemctl enable strongswan

sudo systemctl stop strongswan
sudo systemctl start strongswan
sudo systemctl status strongswan-starter
```

### Firewall rule
```
# accept ports 500 and 4500, required for IKEv2
sudo iptables -A INPUT -p udp --dport  500 -j ACCEPT
sudo iptables -A INPUT -p udp --dport 4500 -j ACCEPT
```
* https://mihai.fm/strongswan-vpn-setup/
* https://forums.raspberrypi.com/viewtopic.php?p=704519
* https://www.vanwerkhoven.org/blog/2018/strongswan-ikev2-vpn-on-raspberry-pi/#etcipsecconf
* https://serverfault.com/questions/1066598/iphone-users-does-not-connect-to-strongswan-vpn-while-android-and-windows-10-us

### TPM
* https://github.com/Infineon/optiga-tpm-cheatsheet
* https://github.com/Infineon/optiga-tpm-explorer/blob/python3_dev/User%20Guide.md
* https://wiki.strongswan.org/projects/strongswan/wiki/TpmPlugin/158

```
tpm2_createek -c 0x81010001 -G rsa -u ek.pub
tpm2_createak -C 0x81010001 -c ak.ctx -u ak.pub -n ak.name
tpm2_evictcontrol -C o -c ak.ctx 0x81010002
tpm2_getcap handles-persistent
```

## Design
* Defence in Depth
* Least Privilege
* Separation of Duties
* Security by Design
* Keep it Simple (Harder than needed - not easy for bad guy)
   * Harder to do the right thing than to do the wrong thing
* Security By Obscurity - Very Bad
* Security by Isolation 

## Signature Generation
> Signature generation is done with the Private Key.
> Signature Verification is done with the Public Key.

## CSR Generation
* CSR is signed with the public key.
* Before creating certificate CSR signature is verified with the Public key contained in the CSR.
* Smart card CSR has subject identifier which is used for whitelisting.
* CSR subject has country C.
* It is possible to change subject while signing CSR.

## Homomorphic Encryption 

* Mathematical Property 
* *7
* (a+b)*7 = 7*a + 7*b

## openssl

OpenSSL provides 2 ways to generate certificates:

1. x509
2. ca

It is possible to change subject field in certificate.

### Openssl commands

```bash
openssl req -new -key your_private_key.key -out your_csr.csr -subj "/C=US/ST=State/L=City/O=Organization/OU=Organizational Unit/CN=Common Name"
openssl x509 -req -in your_csr.csr -CA your_ca_cert.crt -CAkey your_ca_private_key.key -CAcreateserial -out your_certificate.crt -days 365
```

### Openssl HSM Interaction

> It is possible to perform Public Key encryption with the PKCS11 Engine interface with the key stored in HSM.
> It is possible to perform Signature Operation with the PKCS11 Engine interface with the key stored in HSM.
> It is possible to perform Signature Verification with the PKCS11 Engine interface with the key stored in HSM.

### Openssl RSA Encrypt/Decrypt

```bash
openssl pkeyutl 
openssl pkeyutl -decrypt -inkey key.pem -in file -pkeyopt rsa_padding_mode:oaep -pkeyopt rsa_oaep_md:sha256 -out secret
```

## Process

* Secure storage of data and materials

### AES

#### AES CBC

```text
Plaintext Block 1      Plaintext Block 2      Plaintext Block 3      Plaintext Block 4
       |                      |                      |                      |
       v                      v                      v                      v
+--------------+       +--------------+       +--------------+       +--------------+
|   XOR with   |       |   XOR with   |       |   XOR with   |       |   XOR with   |
| Initialization|       |  Ciphertext 1|       |  Ciphertext 2|       |  Ciphertext 3|
|    Vector     |       |              |       |              |       |              |
+--------------+       +--------------+       +--------------+       +--------------+
       |                      |                      |                      |
       v                      v                      v                      v
+--------------+       +--------------+       +--------------+       +--------------+
|    Encrypt   |       |    Encrypt   |       |    Encrypt   |       |    Encrypt   |
|    with Key  |       |    with Key  |       |    with Key  |       |    with Key  |
+--------------+       +--------------+       +--------------+       +--------------+
       |                      |                      |                      |
       v                      v                      v                      v
Ciphertext Block 1      Ciphertext Block 2      Ciphertext Block 3      Ciphertext Block 4
       |                      |                      |                      |
       v                      v                      v                      v
```

#### XOR Truth table

```text

A	B	A XOR B
0	0	0
0	1	1
1	0	1
1	1	0

Explanation:
0 XOR 0 results in 0 because both inputs are the same.
0 XOR 1 results in 1 because the inputs are different.
1 XOR 0 results in 1 because the inputs are different.
1 XOR 1 results in 0 because both inputs are the same.
```

#### AES-GCM (Galois/Counter Mode) 
AES-GCM is an authenticated encryption mode that combines the AES block cipher with Galois field multiplication for authentication. Unlike simple logical operations like XOR, AES-GCM involves complex cryptographic operations and does not have a simple truth table. However, I can provide a high-level overview of how AES-GCM works:

### AES-GCM Overview

1. **Initialization**:
   * A unique Initialization Vector (IV) is generated for each encryption operation.
   * A counter is initialized, typically starting from 1.

2. **Encryption**:
   * The plaintext is divided into blocks.
   * Each block is encrypted using AES in counter mode (AES-CTR).
   * The counter is incremented for each block.

3. **Authentication**:
   * The ciphertext blocks are authenticated using Galois field multiplication.
   * Additional authenticated data (AAD) can be included in the authentication process.
   * A tag is generated to ensure the integrity and authenticity of the ciphertext and AAD.

### AES-GCM Process

```text
Plaintext Block 1      Plaintext Block 2      Plaintext Block 3      Plaintext Block 4
       |                      |                      |                      |
       v                      v                      v                      v
+--------------+       +--------------+       +--------------+       +--------------+
|    Encrypt   |       |    Encrypt   |       |    Encrypt   |       |    Encrypt   |
|    with Key  |       |    with Key  |       |    with Key  |       |    with Key  |
|  (AES-CTR)   |       |  (AES-CTR)   |       |  (AES-CTR)   |       |  (AES-CTR)   |
+--------------+       +--------------+       +--------------+       +--------------+
       |                      |                      |                      |
       v                      v                      v                      v
Ciphertext Block 1      Ciphertext Block 2      Ciphertext Block 3      Ciphertext Block 4
       |                      |                      |                      |
       v                      v                      v                      v
+-------------------------------------------------+-------------------------+
|                  Galois Field Multiplication (Authentication)             |
+-------------------------------------------------+-------------------------+
       |
       v
Authentication Tag
```

### Key Points

* **AES-CTR**: AES in counter mode is used for encryption, where each plaintext block is XORed with the encrypted counter value.
* **Galois Field Multiplication**: Used for authentication, ensuring the integrity and authenticity of the ciphertext and any additional data.
* **Initialization Vector (IV)**: A unique value used for each encryption operation to ensure security.
* **Authentication Tag**: A tag generated during the authentication process, which is used to verify the integrity and authenticity of the data.

AES-GCM provides both confidentiality and authenticity, making it a widely used mode for secure communication.

#### AES-CTR mode

```text
Plaintext Block 1      Plaintext Block 2      Plaintext Block 3      Plaintext Block 4
       |                      |                      |                      |
       v                      v                      v                      v
+-------------------+       +-------------------+       +-------------------+       +-------------------+
|   Counter Block   |       |   Counter Block   |       |   Counter Block   |       |   Counter Block   |
|       1           |       |       2           |       |       3           |       |       4           |
+-------------------+       +-------------------+       +-------------------+       +-------------------+
       |                      |                      |                      |
       v                      v                      v                      v
+-------------------+       +-------------------+       +-------------------+       +-------------------+
|   Encrypt with    |       |   Encrypt with    |       |   Encrypt with    |       |   Encrypt with    |
|     AES Key       |       |     AES Key       |       |     AES Key       |       |     AES Key       |
|   (AES-CTR Mode)  |       |   (AES-CTR Mode)  |       |   (AES-CTR Mode)  |       |   (AES-CTR Mode)  |
+-------------------+       +-------------------+       +-------------------+       +-------------------+
       |                      |                      |                      |
       v                      v                      v                      v
+-------------------+       +-------------------+       +-------------------+       +-------------------+
|  Encrypted Counter|       |  Encrypted Counter|       |  Encrypted Counter|       |  Encrypted Counter|
|       Block 1     |       |       Block 2     |       |       Block 3     |       |       Block 4     |
+-------------------+       +-------------------+       +-------------------+       +-------------------+
       |                      |                      |                      |
       v                      v                      v                      v
+-------------------+       +-------------------+       +-------------------+       +-------------------+
|       XOR         |       |       XOR         |       |       XOR         |       |       XOR         |
|   with Plaintext  |       |   with Plaintext  |       |   with Plaintext  |       |   with Plaintext  |
|     Block 1       |       |     Block 2       |       |     Block 3       |       |     Block 4       |
+-------------------+       +-------------------+       +-------------------+       +-------------------+
       |                      |                      |                      |
       v                      v                      v                      v
+-------------------+       +-------------------+       +-------------------+       +-------------------+
| Ciphertext Block  |       | Ciphertext Block  |       | Ciphertext Block  |       | Ciphertext Block  |
|        1          |       |        2          |       |        3          |       |        4          |
+-------------------+       +-------------------+       +-------------------+       +-------------------+
```

### Linux Capabilities

* Give fine grained access control to the process without giving full root privilage.

### Points to Remember

* Elliptic Curve, Private key is a random number in the range of 0<= k <= n-1
  * n - Order of Basepoint
* Elliptic Curve, Base point is fixed
* Elliptic Curve, Public key = k.G
* IV and Nonce server different purpose
  * IV is Random number
* Nounce is non repeating number
* IV length is fixed to 16 bytes
* AES Block sizei s alwasys 16 bytes irrespective of key size.
* AES 128, 256 all have the same Block size
* SHA256 is 32 bytes
* SM2 has both Signature and Encryption Scheme
* Padding extension attack is not appicable for GCM
* CTR has an issue changing one byte in a block
* GCM and CTR are stread cipher
* NIST P-256 and SECP256R1 are the same
* SECP256R1 - Standards for Efficient Cryptography Prime curve 256-bit Random 1
* GCM uses AES CTR Mode for encryption
* GCM Encryption, Produces Authentication Tag and Encrypted Data as output
* GCM Decryption, Share Nounce, Authentication Tag and Encrypted Data to Decrypt Function
* Format Preserving Encryption - uses token
