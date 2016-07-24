import math as m
import numpy as np
import isprime as isp
import warnings

# warnings.filterwarnings('ignore')

def findBroPrime(prime):
	foundPrime = False
	index = 0
	temp_prime = prime + 1
	while foundPrime == False:
		if isp.isPrime(temp_prime):
			foundPrime = True
			# print index, temp_prime
			return temp_prime
		elif index >= 62:
			return "None found with index at most 62"
		else:
			index += 1
			temp_prime = prime + np.power(2,index)
		if index % 1 ==0: print index, temp_prime

