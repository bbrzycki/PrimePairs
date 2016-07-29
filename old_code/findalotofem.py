import math as m
import numpy as np
import isprime as isp
import findbroprime as f
import primesieve.numpy as ps 

Prime_Limit = np.load("prime_list.npy")

def runOnPrimes(start,stop,index_limit):
	count = 0
	for i in xrange(start,stop+1):
		if isp.isPrime(i):
			bro_candidate = f.findBroPrime(i,index_limit)
			#print i, bro_candidate
			if bro_candidate == -1:
				count += 1
	return count

#print runOnPrimes(2,1000000,30)

def runOnPrimesSet(start,stop,index_limit):
	count = 0
	broprimes = set()
	for i in xrange(start,stop+1):
		if isp.isPrime(i):
			broprimeFound = False
			for (a,b) in broprimes:
				if i == a:
					#print a, b
					broprimeFound = True
				elif i == b:
					#print b, a
					broprimeFound = True
			bro_candidate = f.findBroPrime(i,index_limit)
			if bro_candidate == -1:
				#print "Yikes, nothing above me: ", i
				if broprimeFound == False:
					#print "Not found for ", i, "!!"
					count += 1
					#return -1
			else:
				broprimes.add((i,f.findBroPrime(i,index_limit)))
				#print i, bro_candidate
	return count

def runOnPrimesArray(start,stop,index_limit,prime_list):
	count = 0
	for i in xrange(start,stop+1):
		if isp.isPrimeArray(i,prime_list):
			bro_candidate = f.findBroPrimeArray(i,index_limit,prime_list)
			#print i, bro_candidate
			if bro_candidate == -1:
				count += 1
	return count

print runOnPrimesArray(2,1000000,30,Prime_Limit)

#runOnPrimes(2,1000000,62)

def runOnPrimesSetArray(start,stop,index_limit,prime_list):
	count = 0
	broprimes = set()
	for i in xrange(start,stop+1):
		if isp.isPrime(i,prime_list):
			broprimeFound = False
			for (a,b) in broprimes:
				if i == a:
					#print a, b
					broprimeFound = True
				elif i == b:
					#print b, a
					broprimeFound = True
			bro_candidate = f.findBroPrimeArray(i,index_limit,prime_list)
			if bro_candidate == -1:
				#print "Yikes, nothing above me: ", i
				if broprimeFound == False:
					#print "Not found for ", i, "!!"
					count += 1
					#return -1
			else:
				broprimes.add((i,f.findBroPrimeArray(i,index_limit,prime_list)))
				#print i, bro_candidate
	return count

#runOnPrimesSet(2,1000000,62)