# RSA implementation (Python)

Implementation of the algorithms defined by the RSA scheme as a Command Line Utility.
Computes ciphertext from message and Computes message from ciphertext granted access to secret 
decryption key by using Extended Euclidean Algorithm, Unicode Points,
Modular Arithmetic  and [Modular Exponentiation](https://en.wikipedia.org/wiki/Modular_exponentiation)

## Setup
```sh
pip install primesieve
pip install prsa
```

## What is the RSA Scheme?

[RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) is one of the first practical public-key 
cryptosystems and is widely used for secure data transmission. In this cryptosystem, the encryption key 
is public and differs from the decryption key which is kept secret. In RSA, this asymmetry is based on 
the practical difficulty of factoring the product of two large prime numbers, the factoring problem. 
RSA is made of the initial letters of the surnames of Ron Rivest, Adi Shamir, and Leonard Adleman - The minds behind
the RSA Scheme.

## Usage

**Help**

```sh
~$ prsa -h
usage: PRSA [-h] {decrypt,encrypt,generate} ...

Implementation of the algorithms defined by the RSA scheme in Python3.
Computes ciphertext from message and Computes message from ciphertext granted
access to secret decryption key by using Extended Euclidean Algorithm, Unicode
Points, Modular Arithmetic and Modular Exponentiation

positional arguments:
  {decrypt,encrypt,generate}
    decrypt             Decrypt ciphertext using RSA
    encrypt             Encrypt message using RSA
    generate            Find a key pair given the two natural numbers

optional arguments:
  -h, --help            show this help message and exit
```

**Generate Help**

```sh
~$ prsa generate -h
usage: PRSA generate [-h] p q

positional arguments:
  p           An integer for setting a prime (p)
  q           An integer for setting a prime (q)

optional arguments:
  -h, --help  show this help message and exit
```

**Encrypt Help**

```
~$ prsa encrypt -h
usage: PRSA encrypt [-h] M e n

positional arguments:
  M           Message to be encrypted
  e           A natural number that serves as the first element of the public
              key
  n           A natural number that serves as the second element of the
              private key

optional arguments:
  -h, --help  show this help message and exit
```
**Decrypt Help**

```
~$ prsa decrypt -h
usage: PRSA decrypt [-h] C d n

positional arguments:
  C           Encoded ciphertext to be decrypted
  d           A natural number that serves as the first element of the private
              key
  n           A natural number that serves as the second element of the
              private key

optional arguments:
  -h, --help  show this help message and exit
```

## Example

**Generate Keys, Encrypt 'msg' and then Decrypt**
 
```sh
~$ prsa generate 31974198 84197413
   {
	'Public': [579312365, 1042765315429168511L], 
	'Private': [802880348865349973L, 1042765315429168511L],
   }

~$ prsa encrypt "msg" 579312365 1042765315429168511
   585349761260265530

~$ prsa decrypt 585349761260265530 802880348865349973 1042765315429168511
   msg
```

## Contributing

Bug reports and pull requests are welcome on GitHub at [@ridwanmsharif](https://www.github.com/ridwanmsharif)

## Author

Ridwan M. Sharif: [E-mail](ridwanmsharif@hotmail.com), [@ridwanmsharif](https://www.github.com/ridwanmsharif)

## License

The command line utility is available as open source under the terms of
the [MIT License](https://opensource.org/licenses/MIT)
