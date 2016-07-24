import findalotofem as f 
import matplotlib.pyplot as plt
import numpy as np

def varyIndex(maxindex, limit, step = 1): 
    f1_domain = np. arange ( 0, maxindex + 1, step)
    f4 = lambda n: f.runOnPrimes(2, limit, n)   
    plt. plot ( f1_domain , map(f4, f1_domain), 'bx' )
    plt.show()
    return
    
def varyLimit(maxlimit, index, step = 1): 
    f1_domain = np. arange ( 0, maxlimit + 1, step)
    f4 = lambda n: f.runOnPrimes(2, n, index)   
    plt. plot ( f1_domain , map(f4, f1_domain), 'bx' )
    plt.show()
    return 

varyLimit(100000, 30, 5000) 