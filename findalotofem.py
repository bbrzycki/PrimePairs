import math as m
import numpy as np
import isprime as isp
import findbroprime as f

def runOnPrimes(start,stop):
	for i in xrange(start,stop+1):
		if isp.isPrime(i):
			print i, f.findBroPrime(i)
	return 

