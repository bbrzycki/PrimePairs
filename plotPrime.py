import findalotofem as f 
import matplotlib.pyplot as plt
import numpy as np

def varyIndex(maxindex, limit, step = 1): 
    plt.figure()
    f1_domain = np. arange ( 0, maxindex + 1, step)
    f4 = lambda n: f.runOnPrimes(2, limit, n)   
    plt. plot ( f1_domain , map(f4, f1_domain), 'ro' )
    plt.show()
    return
    
def varyLimit(maxlimit, index, step = 2000): 
    plt.figure()
    f1_domain = np. arange ( 0, maxlimit + 1, step)
    f4 = lambda n: f.runOnPrimes(2, n, index)   
    plt. plot ( f1_domain , map(f4, f1_domain), 'bx' )
    plt.show()
    return

def varyIndexSet(stop, maxindex, step = 1):
    plt.figure()
    f1_domain = np. arange ( 0, maxindex + 1, step)
    f4 = lambda n: f.runOnPrimesSet(2, stop, n)
    plt. plot ( f1_domain , map(f4, f1_domain), 'bx' )
    plt.show()
    return

def varyLimitSet(maxstop, index, step = 5000):
    plt.figure()
    f1_domain = np. arange ( 0, maxstop + 1, step)
    f4 = lambda n: f.runOnPrimesSet(2, n, index)
    plt. plot ( f1_domain , map(f4, f1_domain), 'bx' )
    plt.show()
    return

varyLimitSet(30000, 10, 1000)
onclick(plt.close())