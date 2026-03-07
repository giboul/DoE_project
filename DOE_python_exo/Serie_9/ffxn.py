import numpy as np

#In the order and the number of level of the full factorial model
#Out the full factorial model matrix
def ffxn(order,level):
    mat=[]
    val=np.linspace(-1,1,level)
    print(val)
    for i in range(order):
        tmp=[]
        for j in val:
            tmp+=[j]*int(np.power(level,order-i-1))
        mat+=[tmp*int(np.power(level,i))]
    return np.array(mat).T
    
#Example
print(ffxn(3,3))