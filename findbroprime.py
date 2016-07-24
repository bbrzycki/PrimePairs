import math as m
import numpy as np
import isprime as isp

def findBroPrime(prime):
	foundPrime = False
	index = 0
	temp_prime = prime + 1
	while foundPrime == False:
		if isp.isPrime(temp_prime):
			foundPrime = True
			print index, temp_prime
			return temp_prime
		else:
			index += 1
			temp_prime = prime + np.power(2, index)