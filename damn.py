import math as m
import numpy as np
from bisect import bisect_left

prime_list = np.load("prime_list.npy")


# source: http://stackoverflow.com/questions/212358/binary-search-bisection-in-python
def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)   
    pos = bisect_left(a,x,lo,hi)          # find insertion position
    return (True if pos != hi and a[pos] == x else False) # don't walk off the end

def isPrimeArray(number):
	if number <= 2**32:
		return binary_search(prime_list,number)
	else:
		for prime in prime_list:
			if number % prime == 0:
				return False
		return True

def isPrimeArray1(number):
	if number <= 2**32:
		if number in np.nditer(prime_list):
			return True
		else:
			return False
	else:
		for prime in np.nditer(prime_list):
			if number % prime == 0:
				return False
		return True

# make sure index_limit <= 62
def findBroPrimeArray(prime, index_limit):
	foundPrime = False
	index = 0
	temp_prime = prime + 1
	while foundPrime == False:
		if isPrimeArray(temp_prime):
			foundPrime = True
			# print index, temp_prime
			return temp_prime, index
		elif index >= index_limit:
			#print "No bigbroprime found for ", prime, " with index at most 62."
			return -1
		else:
			index += 1
			temp_prime = prime + 2**index
			# temp_prime = prime + np.power(2,index)
		# if index % 1 ==0: print index, temp_prime

# make sure index_limit <= 62
def findBroPrimeArray1(prime, index_limit):
	foundPrime = False
	index = 0
	temp_prime = prime - 1
	while foundPrime == False:
		if isPrimeArray(temp_prime):
			foundPrime = True
			# print index, temp_prime
			return temp_prime, index
		elif temp_prime<=0:
			#print "No bigbroprime found for ", prime, " with index at most 62."
			return -1
		else:
			index += 1
			temp_prime = prime - 2**index
			# temp_prime = prime + np.power(2,index)
		# if index % 1 ==0: print index, temp_prime

def runOnPrimesArray(start,stop,index_limit):
	count = 0
	catchemall = set()
	for i in xrange(start,stop+1):
		if isp.isPrimeArray(i):
			bro_candidate = f.findBroPrimeArray(i,index_limit)
			#print i, bro_candidate
			if bro_candidate == -1:
				count += 1
				catchemall.add(i)
	return count, catchemall

def runOnPrimesSetArray(start,stop,index_limit):
	count = 0
	broprimes = set()
	catchemall = set()
	for i in xrange(start,stop+1):
		print "..."+str(i)
		if isPrimeArray(i):
			broprimeFound = False
			for (a,b) in broprimes:
				if i == a:
					# print a, b
					broprimeFound = True
				elif i == b:
					# print b, a
					broprimeFound = True
			bro_candidate = findBroPrimeArray(i,index_limit)
			if bro_candidate == -1:
				# print "Yikes, nothing above me: ", i
				if broprimeFound == False:
					# print "Not found for ", i, "!!"
					count += 1
					catchemall.add(i)
					#return -1
			else:
				broprimes.add((i,bro_candidate))
				# print i, bro_candidate
	return count, catchemall

#runOnPrimesSet(2,1000000,62)

# 47867742232066880047611079