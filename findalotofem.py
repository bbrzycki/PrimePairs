import math as m
import numpy as np
import isprime as isp
import findbroprime as f

def runOnPrimes(start,stop):
	count = 0
	for i in xrange(start,stop+1):
		if isp.isPrime(i):
			bro_candidate = f.findBroPrime(i)
			#print i, bro_candidate
			if bro_candidate == -1:
				count += 1
	return count

print runOnPrimes(2,1000000)

def runOnPrimesSet(start,stop):
	broprimes = set()
	for i in xrange(start,stop+1):
		if isp.isPrime(i):
			broprimeFound = False
			for (a,b) in broprimes:
				if i == a:
					print a, b
					broprimeFound = True
				elif i == b:
					print b, a
					broprimeFound = True
			bro_candidate = f.findBroPrime(i)
			if broprimeFound == False:
				
				if bro_candidate == -1:
					print "Not found for ", i, "!!"
				else:
					print i, bro_candidate
			if bro_candidate == -1:
					print "Not found for ", i, "!!"
			elif bro_candidate != -1:
				broprimes.add((i,f.findBroPrime(i)))
				print i, bro_candidate
	return

#runOnPrimesSet(2,1000)