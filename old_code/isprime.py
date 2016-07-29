import math as m
import numpy as np

def isPrime(number):
	if number <= 1: return False
	elif number <= 3: return True
	elif number % 2 == 0 or number % 3 == 0: return False
    	i = 5
    	while i**2 <= number:
        	if number % i == 0 or number % (i + 2) == 0:
			return False
        	i = i + 6
	return True

def isPrimeArray(number, prime_list):
	if number in prime_list:
		return True
	elif number < prime_list[-1]:
		return False
	else:
		for prime in prime_list:
			if number % prime == 0:
				return False
		if number <= 1: return False
		elif number <= 3: return True
		elif number % 2 == 0 or number % 3 == 0: return False
    		i = max(5,prime_list[-1])
    		while i**2 <= number:
        		if number % i == 0 or number % (i + 2) == 0:
				return False
        		i = i + 6
		return True