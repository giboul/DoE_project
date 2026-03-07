import pandas #for dataframe
from math import pi
import math #always useful
import numpy as np #always useful (linear algebra expecially)
import scipy #for various mathematical function you may want
import statsmodels.api as sm #The most complete python pluggin 
#                             for statistical modeling in my sense
from statsmodels.formula.api import ols #For ordinary least square 
#                                       "ols" 
anova_lm = sm.stats.anova_lm #The anova function from statsmodels

#In: E, the essay matrix
#    sig, the std on the measurement (scalar)
#    alpha (optionnal),the effects (chosen randomly between -1 and 1 if empty)
#Out    Y, the randomly (normaly) generated measuremnts
def measurement(E,sig,alpha=None):
    rng = np.random.default_rng()
    # print(E)
    def MU(E,alpha):
        X=np.c_[np.ones(len(E)),E]
        # print(E.shape)
        for i in range(len(E[0])):
            for j in range(i+1,len(E[0])):
                X=np.c_[X,np.multiply(E[:,i],E[:,j]).T]
        return X.dot(alpha)
    E=np.asarray(E)
    n=1 #directly with the cst
    for i in range(1,len(E[0])+1):
        n+=i #add until the total sum of parameters
    if alpha is None:
        alpha=np.random.rand(n)*2-1
        print("Random alpha:",alpha)
    elif len(alpha)!=n:
        print("error alpha not at the right dimension in fct measurment()")
        exit()
    mu=MU(E,alpha)
    print((mu*sig))
    # print(E.shape)
    print((mu))
    Y=rng.normal(mu,np.abs(mu*sig),size=None)
    return Y






E=scipy.linalg.hadamard(8)[:,1:]
full_E=E



n=1
for i in range(1,len(E[0,:5])+1):
    n+=i #add until the total sum of parameters
alpha=np.array(np.random.rand(n)*2-1)
print(alpha)
# alpha=np.array([100,-5,-10,12,-1,2,10,2,0,0,0,0,0,0,0,0])
# print(alpha.shape)

Y=measurement(full_E[:,:5],0.01,alpha=alpha)
# df=pandas.DataFrame(data={"Y":Y,"x1"=full_E[:][0],"x2"=full_E[:][1],"x3"=full_E[:][2],"x4"=full_E[:][3],"x5"=full_E[:][4],"x6"=full_E[:][5],"x7"=full_E[:][6],"x8"=full_E[:][7]})
df=pandas.DataFrame(data=np.c_[Y,full_E],columns=["c0","c1","c2","c3","c4","c5","c6","c7"])
print(df)
formula='c0 ~ c1 + c2 + c3 + c4 + c5'
# formula='c0 ~ c1 + c2 + c3 + c4 + c5 + c6 + c7'
model=ols(formula,data=df)
fitted=model.fit()
print(fitted.summary())
table1=anova_lm(fitted,typ=2)
print(table1)




E=scipy.linalg.hadamard(8)[:,1:]
full_E=np.r_[E,-E]
print(full_E)
Y=measurement(full_E[:,:5],0.01,alpha=alpha)
# df=pandas.DataFrame(data={"Y":Y,"x1"=full_E[:][0],"x2"=full_E[:][1],"x3"=full_E[:][2],"x4"=full_E[:][3],"x5"=full_E[:][4],"x6"=full_E[:][5],"x7"=full_E[:][6],"x8"=full_E[:][7]})
df=pandas.DataFrame(data=np.c_[Y,full_E],columns=["c0","c1","c2","c3","c4","c5","c6","c7"])
print(df)
formula='c0 ~ c1 + c2 + c3 + c4 + c5'
# formula='c0 ~ c1 + c2 + c3 + c4 + c5 + c6 + c7'
model=ols(formula,data=df)
fitted=model.fit()
print(fitted.summary())
table1=anova_lm(fitted,typ=2)
print(table1)

formula='c0 ~ c1*c2 + c1*c3 + c1*c4 + c1*c5 + c2*c3 + c2*c4 + c2*c5 + c3*c4 + c3*c5 + c4*c5 '
# formula='c0 ~ c1*c2 + c1*c3 + c1*c4 + c1*c5 + c1*c6 + c1*c7 + c2*c3 + c2*c4 + c2*c5 + c2*c6 + c2*c7 + c3*c4 + c3*c5 + c3*c6 + c3*c7 + c4*c5 + c4*c6 + c4*c7 + c5*c6 + c5*c7 + c6*c7'
model=ols(formula,data=df)
fitted=model.fit()
print(fitted.summary())
table1=anova_lm(fitted,typ=2)
print(table1)
print(alpha)