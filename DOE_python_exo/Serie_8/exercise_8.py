import pandas #for dataframe
from math import pi
import math #always useful
import matplotlib as mpl # for plot
import matplotlib.pyplot as plt # for plot
import numpy as np #always useful (linear algebra expecially and sampling)
import scipy #for various mathematical function you may want and hadamard matrices
import statsmodels.api as sm #The most complete python package for statistical modeling in my sense
import pyDOE # Warning lot of compatibility problem (useless in 2022 but may corrected in the future)
import itertools
import sympy
#Functions
#                             
from statsmodels.formula.api import ols #For ordinary least square "ols" 
from scipy.optimize import curve_fit # for various fit e.g linear fit
anova_lm = sm.stats.anova_lm #The anova function from statsmodels
incdf= scipy.stats.norm.ppf# inverse of the normal cumulative function 

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
           formula+= " + np.power("+col+",2)"
   else:
       print("Error in Wilkinson Unknown model in input")
       exit()
   return formula
   
def consecutive_anova(mdl,data,pvalue=0.05,print_step=False):
    mod=ols(mdl,data=data)
    fit_model=mod.fit()
    if any(np.isinf(fit_model.bse)):
        print("Error: Too many parameter to fit for the data size")
        print("Anova impossible -> exit")
        exit()
    T_anova=anova_lm(fit_model,typ=2)
    if print_step:print(T_anova)
    max_p=0.
    id_mp=0
    for i in range(len(T_anova["PR(>F)"])):
        if T_anova["PR(>F)"][i]>max_p: 
            max_p=T_anova["PR(>F)"][i]
            id_mp=i
    if max_p>pvalue:
        new_mdl=mdl+" -"+str(T_anova.index.values[id_mp])
        # print(new_mdl)
        return consecutive_anova(new_mdl,data,pvalue,print_step)
    else:
        return T_anova, fit_model

def doehlert(k):
    
    # Fonction génerant une matrice de doehlert pour k facteurs
    #
    #
    # RC LESO-PB 8/12/95
    #
    # Calcul du nombre d'experience:
    N = k*(k+1)+1
    
    # Preparation de la matrice Z
    Z = np.diag(np.ones(k+1),0)
    Z = Z - np.c_[np.ones(k+1),np.zeros((k+1,k))]
    C=np.zeros(((k+1)*k-k,k+1));
    i=1;
    for l in range(1,k+1+1):
    	s=1
    	for m in range(1+1,k+1+1):
    		ll=l+m-s;
    		if (ll>(k+1)):
    			ll=2
    			s=l+m-2			
    		if (l!=ll):
    			C[i-1,:] = Z[l-1,:] - Z[ll-1,:]
    			i=i+1
    Z=np.r_[Z,C]
    
    # Preparation de la base orthogonale B
    B=-np.diag(np.ones(k),-1)
    for l in range(1,k+1):
    	for ll in range(l,k+1):
    		B[l-1,ll-1]=1/ll
    B[:,k+1-1]=np.ones(k+1)
    
    # Calcul de la matrice d'experience Mexp
    X=Z.dot(B)
    for l in range(1,k+1):
    	X[:,l-1]=X[:,l-1]*np.sqrt(l/2/(l+1))
    return X[:,:k]
    
test= doehlert(4)
print(test)

c1=[0,-1,1,-0.5,0.5,-0.5,0.5,-0.5,0.5,-0.5,0,0.5,0,-0.5,0.5,-0.5,0,0,0.5,0,0]
c2=[0,0,0,-0.866,0.866,0.866,-0.866,0.2887,0.2887,0.2887,0.5774,0.2887,0.5774,0.2887,0.2887,0.2887,0.5774,0,0.2887,0.5774,0]
c3=[0,0,0,0,0,0,0,-0.8165,0.8165,0.8165,0.8165,-0.8165,-0.8165,-0.2041,0.2041,0.2041,0.2041,-0.6124,-0.2041,-0.2041,0.6124]
c4=[0,0,0,0,0,0,0,0,0,0,0,0,0,-0.7906,0.7906,0.7906,0.7906,0.7906,-0.7906,-0.7906,-0.7906]
Y=[51.74,51.46,51.22,51.72,46.07,45.89,51.72,52.33,45.83,48.83,49.90,55.76,49.27,49.48,46.35,46.19,48.83,47.95,48.18,46.04,44.30]

E=np.c_[c1,c2,c3,c4]
print(E)

fig=plt.figure(1)
ax1=fig.add_subplot(331)
ax1.scatter(c1,c2)

ax2=fig.add_subplot(332)
ax2.scatter(c1,c2)

ax3=fig.add_subplot(333)
ax3.scatter(c1,c3)

ax4=fig.add_subplot(334)
ax4.scatter(c1,c4)

ax5=fig.add_subplot(335)
ax5.scatter(c2,c3)

ax6=fig.add_subplot(336)
ax6.scatter(c2,c4)

ax7=fig.add_subplot(337)
ax7.scatter(c3,c4)


df=pandas.DataFrame(data=np.c_[Y,E],columns=["c0","c1","c2","c3","c4"])
# print(Wilkinson(["c0","c1","c2","c3","c4"],model="quadratic"))
# print(E)

# print(df)
# Wk_mdl=Wilkinson(["c0","c1","c2","c3","c4"],model="interactions")
# mod=ols(Wk_mdl,data=df)
# fit_model=mod.fit()
# print(fit_model.summary())
# print(anova_lm(fit_model,typ=2))

Wk_mdl=Wilkinson(["c0","c1","c2","c3","c4"],model="quadratic")
print(Wk_mdl)
mod=ols(Wk_mdl,data=df)
fit_model=mod.fit()
print(fit_model.summary())

proba=np.array([(i*2+1)/(2*19) for i in range(19)])
coef=fit_model.params[1:]
ind=np.argsort(coef)
print(coef[ind])
# coef=np.c_[fit_model.summary().xname,fit_model.params][ind]
to_plot=np.c_[coef[ind],proba]
rnames=coef[ind].index.values
# print(rnames)
# print(to_plot)
fig=plt.figure()
ax1=fig.add_subplot(121)
ax1.plot(to_plot[:,0],to_plot[:,1],linestyle="",marker=".")
plt.grid()
ax2=fig.add_subplot(122)
ax2.plot(to_plot[:,0],incdf(to_plot[:,1]),linestyle="",marker=".")
for i,j,k in zip(to_plot[:,0]+0.2,incdf(to_plot[:,1]),rnames):
    ax2.text(i,j,k)
for i,j,k in zip(to_plot[:,0]+0.2,to_plot[:,1],rnames):
    ax1.text(i,j,k)
plt.grid()
def lin(x,a):
   p=[]
   for v in x:
       p+=[v*a]
   return p

# Wk_mdl=Wilkinson(["c0","c1","c2","c3","c4"],model="quadratic")+" -c1:c2:c3:c4 -c1:c3:c4 -c1:c2:c4 -c2:c3:c4 -np.sqrt(c4) -np.sqrt(c2) -c1:c2:c3"
# mod=ols(Wk_mdl,data=df)
# fit_model=mod.fit()
# print(fit_model.summary())
# print(anova_lm(fit_model,typ=2))

# coef=fit_model.params[1:]
# ind=np.argsort(coef)
# print(coef[ind])

# proba=np.array([(i*2+1)/(2*len(coef)) for i in range(len(coef))])
# coef=np.c_[fit_model.summary().xname,fit_model.params][ind]
# to_plot=np.c_[coef[ind],proba]
# rnames=coef[ind].index.values
# print(rnames)
# print(to_plot)
# fig=plt.figure()
# ax1=fig.add_subplot(121)
# ax1.plot(to_plot[:,0],to_plot[:,1],linestyle="",marker=".")
# plt.grid()
# ax2=fig.add_subplot(122)
# ax2.plot(to_plot[:,0],incdf(to_plot[:,1]),linestyle="",marker=".")
# for i,j,k in zip(to_plot[:,0]+0.2,incdf(to_plot[:,1]),rnames):
    # ax2.text(i,j,k)
# for i,j,k in zip(to_plot[:,0]+0.2,to_plot[:,1],rnames):
    # ax1.text(i,j,k)
# plt.grid()
# val, sig = curve_fit(lin,to_plot[2:-3,1],incdf(to_plot[2:-3,2]))
# ax2.plot(np.arange(-7,7),lin(np.arange(-7,7),val))

# print(df)
T_anova, model=consecutive_anova(Wk_mdl,data=df,pvalue=0.04,print_step=False)
print(T_anova)
print(model.summary())

a=np.array([-2.8151, -5.3998,0])
A=np.array([[-3.2873,8.4581/2,0],
           [8.4581/2,0,4.6757/2],
           [0,4.6757/2,-5.2103]])
Xs=-1/2*np.linalg.inv(A).dot(a)
Ys=51.6455+a.dot(Xs)+Xs.T.dot(A.dot(Xs))
print(Xs)
print(Ys)
Lambda, Ev= np.linalg.eig(A)
print(Lambda)
print(Ev)

x2,x3,x4 =sympy.symbols('x2 x3 x4')
Y_x2 = Ys + 0.46601109 + Lambda[1]*x3*x3 +Lambda[2]*x4*x4

# p1=sympy.plotting.plot3d(Y_x2, (x3, -1, 1), (x4, -1, 1))
Y_x3 = Ys + 3.33857464 + Lambda[0]*x2*x2 +Lambda[2]*x4*x4

p1=sympy.plotting.plot3d(Y_x3, (x2, -1, 1), (x4, -1, 1))

plt.show()

