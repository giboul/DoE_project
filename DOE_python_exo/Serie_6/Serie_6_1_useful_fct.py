import pandas #for dataframe
from math import pi
import math #always useful
import numpy as np #always useful (linear algebra expecially and sampling)
import scipy #for various mathematical function you may want and hadamard matrices
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

