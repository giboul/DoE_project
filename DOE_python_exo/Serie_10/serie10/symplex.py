import numpy as np
import itertools

#In dimension q,m
#out symplex essay matrix 
def symplex(q,m): #idee codder simplement ligne par ligne
    Base=list(map(lambda k:k/m,range(m+1)))
    l_all=[list(p) for p in itertools.product(Base, repeat=q)]
    l_symp=[]
    for l in l_all:
        if sum(l)==1: l_symp+=[l]
    return np.array(l_symp[::-1])
print(symplex(4,3))    
symp=symplex(4,3)