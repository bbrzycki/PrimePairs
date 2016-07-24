import math as m
import numpy as np

def isPrime(number):
	for i in xrange(2,int(m.sqrt(number))+1):
		if number % i == 0:
			return False
	return True
