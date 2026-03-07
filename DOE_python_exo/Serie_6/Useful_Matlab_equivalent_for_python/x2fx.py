import numpy as np #always useful (linear algebra expecially and sampling)

                           

#In: The Essay matrix and the model ("linear","interactions","quadratic")
#out The matrix of experiment
def x2fx(E,model="linear"):
   E=np.asarray(E)
   if model=="linear":
       X=np.c_[np.ones(len(E)),E]
   elif model=="interactions":
       X=np.c_[np.ones(len(E)),E]
       for i in range(len(E[0])):
           for j in range(i+1,len(E[0])):
               X=np.c_[X,np.multiply(E[:,i],E[:,j]).T]
   elif model=="quadratic":
       X=np.c_[np.ones(len(E)),E]
       for i in range(len(E[0])):
           for j in range(i,len(E[0])):
               X=np.c_[X,np.multiply(E[:,i],E[:,j]).T]
   else:
       print("Error in xf2x. Unknown model in input")
       exit()
   return X

# Example: interactions model
E=[[1,1,1,1],
   [-1,1,1,1],
   [1,-1,1,1],
   [1,1,-1,1],
   [1,1,1,-1]]
X=x2fx(E,"interactions")
print(X)
