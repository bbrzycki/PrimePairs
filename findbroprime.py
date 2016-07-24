import math as m
import numpy as np
import isprime as isp
import warnings

# warnings.filterwarnings('ignore')

# make sure index_limit <= 62
def findBroPrime(prime, index_limit):
	foundPrime = False
	index = 0
	temp_prime = prime + 1
	while foundPrime == False:
		if isp.isPrime(temp_prime):
			foundPrime = True
			# print index, temp_prime
			return temp_prime
		elif index >= index_limit:
			#print "No bigbroprime found for ", prime, " with index at most 62."
			return -1
		else:
			index += 1
			temp_prime = prime + np.power(2,index)
		# if index % 1 ==0: print index, temp_prime

print findBroPrime(2477,61)

#2477+2^61=2305843009213696429