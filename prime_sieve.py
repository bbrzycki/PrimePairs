import numpy as np
import primesieve.numpy as ps 

# def primes2(n):
#     """ Input n>=6, Returns a list of primes, 2 <= p < n """
#     n, correction = n-n%6+6, 2-(n%6>1)
#     sieve = [True] * (n/3)
#     for i in xrange(1,int(n**0.5)/3+1):
#       if sieve[i]:
#         k=3*i+1|1
#         sieve[      k*k/3      ::2*k] = [False] * ((n/6-k*k/6-1)/k+1)
#         sieve[k*(k-2*(i&1)+4)/3::2*k] = [False] * ((n/6-k*(k-2*(i&1)+4)/6-1)/k+1)
#     return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]

x = ps.generate_primes_array(2**32)
np.save("prime_list", x)

# f = open('prime_list.txt','w')
# for i in xrange(1,2**20+1):
#     if i in x:
#         f.write('1')
#     else:
#         f.write('0')
# 
# f.close()

print np.load("prime_list.npy")
#print np.load("prime_list_sieve.npy")
