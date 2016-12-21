import random
from primesieve import *

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