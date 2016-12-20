import random
from primesieve import *
from euclid import *
from encode import *

# Purpose:
# find_e(pot, module) consumes a number and another number and checks if they are
# coprime. If so then it returns the number. Otherwise it moves to the next number
# in the numberline and repeats the process
# Contract: Nat Nat -> Nat
def find_e(pot, module):
	if euclid_gcd(pot, module) == 1:
		x = pot
	else:
		x = find_e((pot + 1), module)
	return x

# Purpose:
# find_d(e, p, q) consumes a number e (look above), and two primes and finds and returns
# a number d that is the multiplicative inverse of e in the modular class of the 
# product of the two input primes
# Contract: Nat Nat Nat -> Nat
def find_d(e, p, q):
	x = extended_euclid(e, ((p - 1) * (q - 1)))
	if x[2] == 1:
		return (x[1] % ((p - 1) * (q - 1)))
	else:
		return "Pick for e not valid"
# Purpose:
# generate_public(p, q) generates a 2 element list representing the public key
# that is [e, n] having given the 2 primes as parameters
# Contract: Num Num -> (listof Num Num)
def generate_public(p, q):
	p1q1 = (p - 1) * (q - 1)
	potential = random.randint(1, p)
	y = find_e(potential, p1q1)
	public_key = [y, (p * q)]
	return public_key

# Purpose:
# generate_private(name, e, p, q) generates a 2 element list representing the private key
# that is [d, n] having given the first element of the public key and 2 primes as parameters
# Contract: Num Num -> (listof Num Num)
def generate_private(e, p, q):
	x = find_d(e, p, q)
	private_key = [x, (p*q)]
	return private_key


# Purpose:
# encrypt_message(message, pkey, n) consumes the message to be sent and the elements of the 
# the public key then proceeds to use it as an exponent on the encoded numerical equivalent
# of the message and reduces it by the modulo of the product of the two primes 
# (i.e the second part of the public key)
# Contract: Str Str -> Int
# Requires: Because of the temporary restriction on encode, message must be only lowercase letters
def encrypt_message(message, pkey, n):
	encoded = encode_message(message)
	ciphertext = pow(encoded, pkey, n)
	return ciphertext

# Purpose:
# decrypt_message(ciphertext, skey, n) consumes the ciphertext recieved and the elements of the
# pricvate key and then proceeds to use it as an exponent on the encoded numerical equivalent
# of the ciphertext and reduces it by the modulo of the product
# of the two primes (i.e the second part of the private key) then finally decodes it
# NOTE: Private Key is only available to the owner of the key. Thus Private.
# Contract: Str Str -> Str
def decrypt_message(ciphertext, skey, n):
	decrypted_text = pow(ciphertext, skey, n)
	if decrypted_text > n:
		final = "Message too long"
	else :
		final = decode_message(decrypted_text)
	return final