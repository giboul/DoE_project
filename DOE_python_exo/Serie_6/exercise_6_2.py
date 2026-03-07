import pandas #for dataframe
from math import pi
import math #always useful
import matplotlib as mpl # for plot
import matplotlib.pyplot as plt # for plot
import numpy as np #always useful (linear algebra expecially and sampling)
import scipy #for various mathematical function you may want and hadamard matrices
import statsmodels.api as sm #The most complete python package for statistical modeling in my sense
import pyDOE # Warning lot of compatibility problem (useless in 2022 but may corrected in the future)

#Functions
#                             
from statsmodels.formula.api import ols #For ordinary least square "ols" 
from scipy.optimize import curve_fit # for various fit e.g linear fit
anova_lm = sm.stats.anova_lm #The anova function from statsmodels
incdf= scipy.stats.norm.ppf# inverse of the normal cumulative function 

#In: The Essay matrix and the model
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

# In: A list of variable name (the dependant variable should the first one) 
#     and a model
# Out: The Wilkinson formulation of the model for the OLS function
def Wilkinson(cols,model="linear"):
   formula=cols[0] + " ~" 
   if model=="linear":
       for col in cols[1:]:
           formula+= " + "+col
   elif model=="interactions":
       formula+= " "+cols[1]
       for col in cols[2:]:
           formula+= "*"+col
   elif model=="quadratic":
       formula+= " "+cols[1]
       for col in cols[2:]:
           formula+= "*"+col
       for col in cols[1:]:
           formula+= " + np.sqrt("+col+")"
   else:
       print("Error in Wilkinson Unknown model in input")
       exit()
   return formula

# In: The order of the model
# Out: the 2-level full fractionnal model of n-th order
def ff2n(order):
    mat=[]
    for i in range(order):
        tmp=[-1]*int(np.power(2,order-i-1))+[1]*int(np.power(2,order-i-1))
        mat+=[tmp*int(np.power(2,i))]
    return np.array(mat).T
    
Y=[19.67, -3.12, 23.55, 2.46, 47.18, 36.7, 61.23, 19.25, -18.59, 40.72, -29.31, 42.6, -29.61, -1.45, -26.47, 4.92]

E=ff2n(4)
# print(np.c_[Y,E])
df=pandas.DataFrame(data=np.c_[Y,E],columns=["c0","c1","c2","c3","c4"])
print(Wilkinson(["c0","c1","c2","c3","c4"],model="quadratic"))
print(E)
mod=ols(Wilkinson(["c0","c1","c2","c3","c4"],model="interactions"),data=df)
fit_model=mod.fit()
print(fit_model.summary())

proba=np.array([(i*2+1)/(2*16) for i in range(16)])
ind=np.argsort(fit_model.params)
print(ind)
coef=fit_model.params
# coef=np.c_[fit_model.summary().xname,fit_model.params][ind]
to_plot=np.c_[coef[ind],proba]
print(to_plot)
fig=plt.figure()
ax1=fig.add_subplot(121)
ax1.plot(to_plot[:,0],to_plot[:,1],linestyle="",marker=".")
plt.grid()
ax2=fig.add_subplot(122)
ax2.plot(to_plot[:,0],incdf(to_plot[:,1]),linestyle="",marker=".")
plt.grid()
def lin(x,a):
   p=[]
   for v in x:
       p+=[v*a]
   return p

# val, sig = curve_fit(lin,to_plot[2:-3,1],incdf(to_plot[2:-3,0]))
# ax2.plot(np.arange(-7,7),lin(np.arange(-7,7),val))

mod=ols("c0 ~ c1 + c4 + c1:c2 + c1:c4 + c1:c2:c4",data=df)
fit_model=mod.fit()
print(fit_model.summary())
print(anova_lm(fit_model,typ=2))

mod=ols("c0 ~ c1 + c4 + c1:c2 + c1:c4",data=df)
fit_model=mod.fit()
print(fit_model.summary())
print(anova_lm(fit_model,typ=2))


plt.show()