#
## tz
* https://blog.quarkslab.com/introduction-to-trusted-execution-environment-arms-trustzone.html
https://prateekvjoshi.com/2015/02/07/why-are-they-called-elliptic-curves/
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
> For example: (11, 13) Here, 11 and 13 are coprime numbers, and their LCM is 11 × 13 = 143 . Because prime numbers only share one common factor, 1, any two prime numbers are always coprime.

#### 
ref.
* https://en.m.wikipedia.org/wiki/Coprime_integers

---
## ec
1. https://cryptobook.nakov.com/digital-signatures/eddsa-and-ed25519
1. https://en.m.wikipedia.org/wiki/Barrett_reduction
1. https://github.com/rweather/arduinolibs/blob/master/libraries/Crypto/Ed25519.cpp#L304
1. https://en.m.wikipedia.org/wiki/Extended_Euclidean_algorithm
1. algebraic curves over finite fields
1. https://www.allaboutcircuits.com/technical-articles/elliptic-curve-cryptography-in-embedded-systems/
1.    https://cryptobook.nakov.com/asymmetric-key-ciphers/elliptic-curve-cryptography-ecc
1.https://medium.com/asecuritysite-when-bob-met-alice/so-what-have-prime-numbers-and-galois-fields-to-do-with-your-privacy-2dff9881361e


### ec
1. https://fission.codes/blog/everything-you-wanted-to-know-about-elliptic-curve-cryptography/
1. https://graui.de/code/elliptic2/
1. https://asecuritysite.com/curve25519/eddsa
1. https://asecuritysite.com/curve25519

#### Elliptic curve Point Addition online
1. https://andrea.corbellini.name/ecc/interactive/modk-add.html

### start here
1. https://andrea.corbellini.name/2015/05/23/elliptic-curve-cryptography-finite-fields-and-discrete-logarithms/

1. https://andrea.corbellini.name/2015/05/17/elliptic-curve-cryptography-a-gentle-introduction/

####
> A finite field is, first of all, a set with a finite number of elements. An example of finite field is the set of integers modulo p
, where 
p is a prime number

> find the multiplicative inverse of a number and then perform a single multiplication.

Computing the multiplicative inverse can be “easily” done with the extended Euclidean algorithm

### tool
1. https://www.dcode.fr/modular-inverse
---
## rsa

> For a positive integer n, define φ(n) to be the number of integers less than n that are relatively prime with n. For example, φ(12) = 4, since only 11, 7, 5 and 1 are less than 12 and relatively prime to 12, while φ(7) = 6. In fact, for any prime number p we have φ(p) = p - 1
1. https://www.cantorsparadise.com/rsa-algorithm-in-depth-mathematical-walk-through-3bf33759022a
1. https://www.di-mgt.com.au/rsa_alg.html#simpleexample
1. https://doctrina.org/How-RSA-Works-With-Examples.html
1. https://cryptobook.nakov.com/asymmetric-key-ciphers/the-rsa-cryptosystem-concepts
1. https://doctrina.org/How-RSA-Works-With-Examples.html#

### multiplicative inverse 
> A multiplicative inverse for x
 is a number that when multiplied by x
, will equal 1
. The multiplicative inverse of x
 is written as x−1
 and is defined as so:

x⋅x−1=1
The greatest common divisor (gcd) between two numbers is the largest integer that will divide both numbers. For example, gcd(4,10)=2
.

The interesting thing is that if two numbers have a gcd of 1, then the smaller of the two numbers has a multiplicative inverse in the modulo of the larger number. It is expressed in the following equation

### chacha20
chacha20 is a stream cipher

### md2 md4 md5 md6
> Message digest algirithm

### SM2
SM2 is actually an elliptic curve based algorithm

### SM3
ShangMi 3 (SM3) is a cryptographic hash function.

### SM4
SM3 block cipher

## online tool
* https://cyberchef.io/

## AES Implementation
* AES 128 Implementaiton

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
* Seperation of Duties
* Security by Design
* Keep it Simple (Harder than needed - not easy for bad guy)
   * Harder to right thing than to do the wrong thing
* Security By Obscurity - Very Bad
## Singnature Generation
> Signature generation is done with the Private Key
> Signature Verification is done with the Public Key
