import random
from primesieve import *
from euclid import *
from encode import *
from cipher import *

# Purpose:
# generate_key_pair(num1, num2): generates a dictionary with 2 elements: The public and 
# private key
# Contract: Nat Nat -> Dict
def generate_key_pair(num1, num2):
	primes = set_primes(num1, num2)
	p = primes[0]
	q = primes[1]

	public = generate_public(p, q)
	private = generate_private(public[0], p, q)
	key_pair = {"Public": public,
				"Private": private}
	return key_pair

# Purpose:
# rsa_encrypt(message, pkey, n) is a wrapper function that generates
# an encoded ciphertext given the elements of any given public key
# It does so by implementing algorithms defined by the RSA Scheme
# Contract: Str Nat Nat -> Nat
def rsa_encrypt(message, pkey, n):
	c = encrypt_message(message, pkey, n)
	return c

# Purpose:
# rsa_decrypt(ciphertext, skey, n) is a wrapper function that generates
# a decoded message given the elements of the required private key
# It does so by implementing algorithms defined by the RSA Scheme
# Contract: Nat Str -> Str
def rsa_decrypt(ciphertext, skey, n):
	r = decrypt_message(ciphertext, skey, n ) 
	return r
