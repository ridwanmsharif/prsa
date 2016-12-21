import random
from primesieve import *
from euclid import *

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