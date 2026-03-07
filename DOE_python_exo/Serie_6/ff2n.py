import numpy as np #always useful (linear algebra expecially and sampling)

# In: The order of the problem (number of variable)
# Out: the n-th order 2-level full factorial design essay matrix
def ff2n(order):
    mat=[]
    for i in range(order):
        tmp=[-1]*int(np.power(2,order-i-1))+[1]*int(np.power(2,order-i-1))
        mat+=[tmp*int(np.power(2,i))]
    return np.array(mat).T
    
#Example : fourth order full factorial model
F=ff2n(5)
print(F)