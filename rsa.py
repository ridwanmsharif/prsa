import random
from primesieve import *


# Purpose:
# set_primes(num1, num2) consumes 2 natural numbers and produces 2
# primes. Each prime p, q will be the nth and kth prime numbers as appears
# in the real number line where n and k are num1 and num2 respectively
# Contract: Nat Nat -> Nat(Prime)
def set_primes(num1, num2):
	p = nth_prime(num1)
	q = nth_prime(num2)
	return p, q

# Purpose:
# encode(message) consumes the message you wish to encode in numbers and
# produces a unique number that represents the message. this number will have 
# length twice that of the message. 
# Numerical value of the number (i.e. magnitude of number is irrelevant)
# Contract: Str -> Nat
# Requires: message consists of only lowercase letters
def encode_message(message):
	encoded_message = ""

	for char in message:
		if (ord(char) - ord('a')) < 10:
			new_letter = ("0" + (str(ord(char) - ord('a'))))
		else:
			new_letter = (str(ord(char) - ord('a')))
		encoded_message += new_letter
	return int(encoded_message)

# Purpose:
# decode(coded) consumes the encoded message you wish to read in numbers and
# produces the unique message. Essentially the opposite of encode, named intuitively 
# for this reason
# Numerical value of the number (i.e. magnitude of number is irrelevant)
# Contract: Nat -> Str
def decode_message(coded):
	coded_cypher = str(coded)
	decoded_message = ""

	if len(coded_cypher) % 2 == 1:
		coded_cypher = '0' + coded_cypher
	else:
		coded_cypher = coded_cypher
	
	for i in range(len(coded_cypher)/2):
		decoded_message = decoded_message + str(chr(int(coded_cypher[2*i:(2*i + 2)]) + ord('a')))
		
	return decoded_message

# Purpose:
# extended_euclid(num1, num2) follows the Extented Euclidean Algorithm to return 
# the coefficients and the Greatest Common Divisor of num1 and num2 of the linear 
# diophantine equation where integer multiples of num1 and num2 sum to give their GCD
# Contract: Int Int -> Int Int Int 
def extended_euclid(num1, num2):
	rem1 = max(num1, num2)
	rem2 = min(num1, num2)
	coeff_big_x, coeff_big_y, coeff_small_x, coeff_small_y = 1, 0, 0, 1

	while rem2 > 0:
		q = rem1 % rem2
		multiplier = rem1/rem2
		rem1, rem2 = rem2, q
		coeff_big_x, coeff_small_x = coeff_small_x, (coeff_big_x - (multiplier * coeff_small_x))
		coeff_big_y, coeff_small_y = coeff_small_y, (coeff_big_y - (multiplier * coeff_small_y))
	return coeff_big_x, coeff_big_y, rem1

# Purpose:
# euclid_gcd(num1, num2) consumes 2 numbers and produces their Greatest Common
# Divisor by using pure structural recursion
# Contract: Int Int -> Nat	
def euclid_gcd(num1, num2):
	if num2 == 0:
		x = num1
	else:
		x = euclid_gcd(num2, (num1 % num2))
	return x

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
