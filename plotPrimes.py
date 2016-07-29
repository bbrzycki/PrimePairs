import damn as d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

def varyIndex(maxindex, limit, step = 1): 
    #plt.figure()
    f1_domain = np. arange ( 0, maxindex + 1, step)
    f4 = lambda n: d.runOnPrimesArray(2, limit, n)[0]
    plt. plot ( f1_domain , map(f4, f1_domain), 'ro' )
    plt.show()
    return
    
def varyLimit(maxlimit, index, step = 2000): 
    #plt.figure()
    f1_domain = np. arange ( 0, maxlimit + 1, step)
    f4 = lambda n: d.runOnPrimesArray(2, n, index)[0]  
    plt. plot ( f1_domain , map(f4, f1_domain), 'bx' )
    plt.show()
    return

def varyIndexSet(pdf, stop, maxindex, step):
    fig = plt.figure()
    fig.suptitle("Number of Primes Without Broprimes vs. Index Bound")
    ax = fig.add_subplot(111)
    title = "Upper bound: "+str(stop)+", index bound: "+str(maxindex)+", step: "+str(step)
    ax.set_title(title)
    ax.set_xlabel("Index bound")
    ax.set_ylabel("Number of primes without broprimes")
    f1_domain = np. arange ( 0, maxindex + 1, step)
    f4 = lambda n: d.runOnPrimesSetArray(2, stop, n)[0]
    ax. plot ( f1_domain , map(f4, f1_domain), 'bx' )
    (a,b) = d.runOnPrimesSetArray(2, stop, maxindex)
    toprighttext = "For N = "+str(maxindex)+", "+str(a)+" prime(s) left: "+", ".join(str(e) for e in b)
    ax.text(.99, .99, toprighttext,
        horizontalalignment='right',
        verticalalignment='top',
        transform=ax.transAxes)
    #filename="indexplot-"+str(stop)+"-"+str(maxindex)+"-"+str(step)+".pdf"
    #plt.savefig(filename, format='pdf')
    pdf.savefig()
    #plt.show()
    return

def varyLimitSet(pdf, maxstop, index, step):
    fig = plt.figure()
    fig.suptitle("Number of Primes Without Broprimes vs. Upper Bound")
    ax = fig.add_subplot(111)
    title = "Upper bound: "+str(maxstop)+", index bound: "+str(index)+", step: "+str(step)
    ax.set_title(title)
    ax.set_xlabel("Upper bound")
    ax.set_ylabel("Number of primes without broprimes")
    f1_domain = np. arange ( 0, maxstop + 1, step)
    f4 = lambda n: d.runOnPrimesSetArray(2, n, index)[0]
    ax. plot ( f1_domain , map(f4, f1_domain), 'bx' )
    #filename="limitplot-"+str(maxstop)+"-"+str(index)+"-"+str(step)+".pdf"
    #plt.savefig(filename, format='pdf')
    pdf.savefig()
    #plt.show()
    return

with PdfPages('indexplots.pdf') as pdf:
    #varyIndexSet(pdf, 1000, 20, 1)
    #varyIndexSet(pdf, 1000, 30, 1)
    #varyIndexSet(pdf, 1000, 40, 1)
    #varyIndexSet(pdf, 1000, 100, 5)
    #varyIndexSet(pdf, 1000, 200, 10)
    #varyIndexSet(pdf, 10000, 20, 1)
    #varyIndexSet(pdf, 10000, 30, 1)
    #varyIndexSet(pdf, 10000, 40, 1)
    #varyIndexSet(pdf, 10000, 50, 1)
    varyIndexSet(pdf, 10000, 60, 1)
    #varyIndexSet(pdf, 100000, 100, 5)

with PdfPages('limitplots.pdf') as pdf:
    varyLimitSet(pdf, 1000, 20, 10)
    varyLimitSet(pdf, 1000, 30, 10)
    varyLimitSet(pdf, 1000, 40, 10)
    #varyLimitSet(pdf, 10000, 20, 50)
    #varyLimitSet(pdf, 10000, 20, 100)
    #varyLimitSet(pdf, 10000, 30, 100)
    #varyLimitSet(pdf, 10000, 40, 100)
    #varyLimitSet(pdf, 10000, 100, 100)
    #varyLimitSet(pdf, 100000, 100, 1000)

#plot.show()