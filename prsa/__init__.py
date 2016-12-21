#!/usr/bin/env python

from rsa import *
from primesieve import *
import argparse


parser = argparse.ArgumentParser(prog='PRSA',
description='''Implementation of the algorithms
defined by the RSA scheme in Python3. Computes ciphertext from message and
Computes message from ciphertext granted access to secret decryption key by
using Extended Euclidean Algorithm, Unicode Points, Modular Arithmetic and 
Modular Exponentiation''', add_help=True)
subparsers = parser.add_subparsers()

decrypt_parser = subparsers.add_parser('decrypt', help='Decrypt ciphertext using RSA')

decrypt_parser.add_argument('ctext', metavar='C', type=int,
        help='Encoded ciphertext to be decrypted')
decrypt_parser.add_argument('privatekey', metavar='d', type=int,
    help='A natural number that serves as the first element of the private key')
decrypt_parser.add_argument('mod', metavar='n', type=int,
        help='A natural number that serves as the second element of the private key')

encrypt_parser = subparsers.add_parser('encrypt', help='Encrypt message using RSA')
encrypt_parser.add_argument('text', metavar='M', type=str,
        help='Message to be encrypted')
encrypt_parser.add_argument('publickey', metavar='e', type=int,
    help='A natural number that serves as the first element of the public key')
encrypt_parser.add_argument('mod', metavar='n', type=int,
    help='A natural number that serves as the second element of the private key')

generate_parser = subparsers.add_parser('generate', 
    help='Find a key pair given the two natural numbers')
generate_parser.add_argument('np', metavar='p', type=int,
    help='An integer for setting a prime (p)')
generate_parser.add_argument('nq', metavar='q', type=int,
    help='An integer for setting a prime (q)')


args = parser.parse_args()
if hasattr(args, 'ctext'):
	print(rsa_decrypt(args.ctext, args.privatekey, args.mod))
elif hasattr(args, 'publickey'):
	print(rsa_encrypt(args.text, args.publickey, args.mod))
else:
    print(generate_key_pair(args.np, args.nq))
