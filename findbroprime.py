import math as m
import numpy as np
import isprime as isp

def findBroPrime(prime):
	foundPrime = False
	temp_prime = prime + 1
	index = 0
	while foundPrime == False:
		