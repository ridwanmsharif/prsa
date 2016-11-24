import random
from primesieve import *

public_keys = {}
private_key = {}

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
# generate_public(name, p, q) generates a slot in the public_keys dictionary previously 
# defined and adds an entry with the Name of the sender as ther Key and the values of e
# and product of the two primes input as parameters as the value stored in that order
# Contract: Str Num Num -> Dict
def generate_public(name, p, q):
	p1q1 = (p - 1) * (q - 1)
	potential = random.randint(1, p)
	y = find_e(potential, p1q1)
	public_keys[name] = [y, (p * q)]
	return public_keys

# Purpose:
# generate_private(name, e, p, q) generates a slot in the private_key dictionary previously 
# defined and adds an entry with the Name of the sender as ther Key and the values of d
# (as calculated) & product of the 2 primes as parameters as the value stored in that order
# Contract: Str Num Num -> Dict
def generate_private(name, e, p, q):
	x = find_d(e, p, q)
	private_key[name] = [x, (p*q)]
	return private_key

# Purpose:
# encrypt_message(message, name) consumes the message to be sent and the name of the recipient
# and then proceeds to look up the recipients public key and uses it as an exponent on the 
# encoded numerical equivalent of the message and reduces it by the modulo of the product
# of the two primes (i.e the second part of the public key)
# Contract: Str Str -> Int
# Requires: Because of the temporary restriction on encode, message must be only lowercase letters
def encrypt_message(message, name):
	encoded = encode_message(message)
	ciphertext = pow(encoded, public_keys[name][0], public_keys[name][1])
	return ciphertext

# Purpose:
# decrypt_message(ciphertext, name) consumes the ciphertext recieved and the name of the recipient
# and then proceeds to look up the recipients private key and uses it as an exponent on the 
# encoded numerical equivalent of the ciphertext and reduces it by the modulo of the product
# of the two primes (i.e the second part of the private key) then finally decodes it
# NOTE: Private Key is only available to the owner of the key. Thus Private.
# Contract: Str Str -> Str
def decrypt_message(ciphertext, name):
	decrypted_text = pow(ciphertext, private_key[name][0], private_key[name][1])
	if decrypted_text > private_key[name][1]:
		final = "Message too long"
	else :
		final = decode_message(decrypted_text)
	return final

# Purpose:
# generate_rsa_message(name, message, num1, num2) is a wrapper function that generates
# an encoded ciphertext given the name of the recipient the message and 2 numbers used to find
# primes as defined by set_primes. It does so by implementing algorithms defined by the RSA Scheme
# Contract: Str Str Nat Nat -> Nat
def generate_rsa_message(name, message, num1, num2):
	primes = set_primes(num1, num2)
	p = primes[0]
	q = primes[1]

	generate_public(name, p, q)
	generate_private(name, public_keys[name][0], p, q)
	c = encrypt_message(message, name)
	return c

# Purpose:
# retrieve_rsa_message(name, ciphertext) is a wrapper function that generates
# a decoded message given the name of the recipient the message and the encoded ciphertext
# It does so by implementing algorithms defined by the RSA Scheme
# Contract: Str Str -> Str
def retrieve_rsa_message(name, ciphertext):
	r = decrypt_message(ciphertext, name) 
	return r

# x = generate_rsa_message('Ridwan', 'ridwan', 123456788, 123456789)
# r = retrieve_rsa_message('Ridwan', x)