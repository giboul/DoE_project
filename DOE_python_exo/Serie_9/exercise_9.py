import pandas as pd#for dataframe
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
from mesure3 import *
import plotly.graph_objects as go # For isosurface plotting https://plotly.com/python/3d-isosurface-plots/



#Functions
#                             
from statsmodels.formula.api import ols #For ordinary least square "ols" 
from scipy.optimize import curve_fit # for various fit e.g linear fit
anova_lm = sm.stats.anova_lm #The anova function from statsmodels
incdf= scipy.stats.norm.ppf# inverse of the normal cumulative function 
eig=np.linalg.eig # compute a matrice eigen values and vectors

# def mdl_2_A(fitted_model)

def ffxn(order,level):
    mat=[]
    val=(np.linspace(0,level,level)*2-level)/level
    print(val)
    for i in range(order):
        tmp=[]
        for j in val:
            tmp+=[j]*int(np.power(level,order-i-1))
        mat+=[tmp*int(np.power(level,i))]
    return np.array(mat).T
    

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
def slice3d(func,x1_lim,x2_lim,const,const_axis="z"):   # derived from https://stackoverflow.com/questions/57483209/how-do-i-highlight-a-slice-on-a-matplotlib-3d-surface-plot
    
    X1,X2=np.mgrid[x1_lim[0]:x1_lim[1]:100j,x2_lim[0]:x2_lim[1]:100j]
    X3=np.ones(X1.shape)*const
    if const_axis=="z":
        vs=F(X1,X2,X3)
    elif const_axis=="y":
        vs=F(X1,X3,X2)
    elif const_axis=="x":
        vs=F(X3,X1,X2)
    else:
        print("error in slice3d: axis must be x, y or z")
    figsl=plt.figure(figsize = (5,6))
    ax = plt.subplot(111, projection='3d')
    # Create array to specify color of each pixel on surface
    vs=(vs-vs.min())/(vs-vs.min()).max()
    cmap = plt.cm.plasma
    # vs=np.sqrt((vs-vs.min())/abs(vs-vs.min()).max())
    # print(vs.tolist())
    # vs=np.log10(abs(vs))/np.log(abs(vs)).max()
    
    # X3=np.ones(X1.shape)*const
    if const_axis=="z":  surf=ax.plot_surface(X1, X2, X3, facecolors=cmap(vs),
                       linewidth=0, antialiased=False)
    elif const_axis=="y":surf=ax.plot_surface(X1, X3, X2, facecolors=cmap(vs),
                       linewidth=0, antialiased=False)
    elif const_axis=="x":surf=ax.plot_surface(X3, X1, X2, facecolors=cmap(vs),
                       linewidth=0, antialiased=False)
    # figsl.colorbar(surf, shrink=0.5, aspect=5)
    # ax.colorbar(mpl.cm.ScalarMappable(cmap=cmap).set_array(vs))
    # ax.colorbar(mpl.cm.ScalarMappable(cmap=cmap).set_array(vs))
    # 2D Plot of slice of 3D plot 
    # Normalise y for calling in the cmap.
    # ys = Ys[:,0]
    # plt.subplot(212)
    # plt.plot(x,Z[10,:], color=cmap(ys[10]))
    # plt.plot(x,Z[20,:], color=cmap(ys[20]))
    
    # plt.savefig('surfacePlotHighlight.png')  
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
    
#Example : fourth order full factorial model
F=ffxn(4,3)
# print(F)
# print(len(F))

Design3k=ffxn(3,3)
Ddoehlert=doehlert(3)
DBox=np.array([[0,0,0,0,-1,-1,1,1,-1,-1,1,1,0],
               [-1,-1,1,1,0,0,0,0,-1,1,-1,1,0],
               [-1,1,-1,1,-1,1,-1,1,0,0,0,0,0]]).T
alpha=1.22
Dcomposite1=ffxn(3,2)
Dcomposite2=np.array([[alpha,0,0],
                      [-alpha,0,0],
                      [0,alpha,0],
                      [0,-alpha,0],
                      [0,0,alpha],
                      [0,0,-alpha],
                      [0,0,0]])
Dcomposite=np.r_[Dcomposite1,Dcomposite2]
print(Dcomposite)      
MDesign3k=mesure3(Design3k)
MDdoehlert=mesure3(Ddoehlert)
MDBox=mesure3(DBox)
MDcomposite=mesure3(Dcomposite)

Wk_mdl="c0 ~ c1*c2*c3 - c1:c2:c3 + np.power(c1,2) + np.power(c2,2) + np.power(c3,2)"
mdl_Design3k=ols(Wk_mdl,data=pd.DataFrame(data=np.c_[MDesign3k,Design3k],columns=["c0","c1","c2","c3"]))
fit_Design3k=mdl_Design3k.fit()
print(fit_Design3k.summary()) 

Wk_mdl="c0 ~ c1*c2*c3 - c1:c2:c3 + np.power(c1,2) + np.power(c2,2) + np.power(c3,2)"
mdl_Ddoehlert=ols(Wk_mdl,data=pd.DataFrame(data=np.c_[MDdoehlert,Ddoehlert],columns=["c0","c1","c2","c3"]))
fit_Ddoehlert=mdl_Ddoehlert.fit()
print(fit_Ddoehlert.summary()) 

Wk_mdl="c0 ~ c1*c2*c3 - c1:c2:c3 + np.power(c1,2) + np.power(c2,2) + np.power(c3,2)"
mdl_DBox=ols(Wk_mdl,data=pd.DataFrame(data=np.c_[MDBox,DBox],columns=["c0","c1","c2","c3"]))
fit_DBox=mdl_DBox.fit()
print(fit_DBox.summary()) 

Wk_mdl="c0 ~ c1*c2*c3 - c1:c2:c3 + np.power(c1,2) + np.power(c2,2) + np.power(c3,2)"
mdl_Dcomposite=ols(Wk_mdl,data=pd.DataFrame(data=np.c_[MDcomposite,Dcomposite],columns=["c0","c1","c2","c3"]))
fit_Dcomposite=mdl_Dcomposite.fit()
print(fit_Dcomposite.summary()) 


params=fit_Design3k.params
A_Design3k=np.array([[params[-3],params[3],params[5]],
            [params[3],params[-2],params[6]],
            [params[5],params[6],params[-1]]])
a_Design3k=np.array([params[1],params[2],params[3]])
a0_Design3k=params[0]
Xs_Design3k=-1/2*np.linalg.inv(A_Design3k).dot(a_Design3k)      
Ys_Design3k=a0_Design3k + Xs_Design3k.dot(a_Design3k) + Xs_Design3k.dot(A_Design3k.dot(Xs_Design3k))
# print(Ys_Design3k)
lambda_Design3k, Ev_Design3k= eig(A_Design3k)
X,Y,Z=np.mgrid[-5:5:100j,-5:5:100j,-5:5:100j]
# printX
V=Ys_Design3k+lambda_Design3k[0] * X * X + lambda_Design3k[1] * Y * Y +lambda_Design3k[2] * Z * Z
print(Ys_Design3k)
print(V)
print(min(V.flatten()))
print(max(V.flatten()))
print(V.shape)
fig1= go.Figure(data=go.Isosurface(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=V.flatten(),
    # isomin=4,
    # isomax=4.2,
    surface_count=5,
    colorbar_nticks=5,
    caps=dict(x_show=False, y_show=False)
    ))

params=fit_Ddoehlert.params
A_Ddoehlert=np.array([[params[-3],params[3],params[5]],
            [params[3],params[-2],params[6]],
            [params[5],params[6],params[-1]]])
a_Ddoehlert=np.array([params[1],params[2],params[3]])
a0_Ddoehlert=params[0]
Xs_Ddoehlert=-1/2*np.linalg.inv(A_Ddoehlert).dot(a_Ddoehlert)      
Ys_Ddoehlert=a0_Ddoehlert + Xs_Ddoehlert.dot(a_Ddoehlert) + Xs_Ddoehlert.T.dot(A_Ddoehlert.dot(Xs_Ddoehlert))
lambda_Ddoehlert, Ev_Ddoehlert= eig(A_Ddoehlert)
X,Y,Z=np.mgrid[-5:5:50j,-5:5:50j,-5:5:50j]
V=Ys_Ddoehlert+lambda_Ddoehlert[0]*X*X++lambda_Ddoehlert[1]*Y*Y++lambda_Ddoehlert[2]*Z*Z
fig2= go.Figure(data=go.Isosurface(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=V.flatten(),
    isomin=Ys_Ddoehlert-.1,
    isomax=Ys_Ddoehlert-2.,
    surface_count=5,
    colorbar_nticks=5,
    caps=dict(x_show=False, y_show=False)
    ))

params=fit_DBox.params
A_DBox=np.array([[params[-3],params[3],params[5]],
            [params[3],params[-2],params[6]],
            [params[5],params[6],params[-1]]])
a_DBox=np.array([params[1],params[2],params[3]])
a0_DBox=params[0]
Xs_DBox=-1/2*np.linalg.inv(A_DBox).dot(a_DBox)      
Ys_DBox=a0_DBox + Xs_DBox.dot(a_DBox) + Xs_DBox.T.dot(A_DBox.dot(Xs_DBox))
lambda_DBox, Ev_DBox= eig(A_DBox)
X,Y,Z=np.mgrid[-5:5:50j,-5:5:50j,-5:5:50j]
V=Ys_DBox+lambda_DBox[0]*X*X++lambda_DBox[1]*Y*Y++lambda_DBox[2]*Z*Z
fig3= go.Figure(data=go.Isosurface(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=V.flatten(),
    isomin=Ys_DBox+.1,
    isomax=Ys_DBox+2.,
    surface_count=5,
    colorbar_nticks=5,
    caps=dict(x_show=False, y_show=False)
    ))

params=fit_Dcomposite.params
A_Dcomposite=np.array([[params[-3],params[3],params[5]],
            [params[3],params[-2],params[6]],
            [params[5],params[6],params[-1]]])
a_Dcomposite=np.array([params[1],params[2],params[3]])
a0_Dcomposite=params[0]
Xs_Dcomposite=-1/2*np.linalg.inv(A_Dcomposite).dot(a_Dcomposite)      
Ys_Dcomposite=a0_Dcomposite + Xs_Dcomposite.dot(a_Dcomposite) + Xs_Dcomposite.T.dot(A_Dcomposite.dot(Xs_Dcomposite))
lambda_Dcomposite, Ev_Dcomposite= eig(A_Dcomposite)
X,Y,Z=np.mgrid[-5:5:50j,-5:5:50j,-5:5:50j]
V=Ys_Dcomposite+lambda_Dcomposite[0]*X*X++lambda_Dcomposite[1]*Y*Y++lambda_Dcomposite[2]*Z*Z
fig4= go.Figure(data=go.Isosurface(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=V.flatten(),
    isomin=Ys_Dcomposite-.1,
    isomax=Ys_Dcomposite-2.,
    surface_count=5,
    colorbar_nticks=5,
    caps=dict(x_show=False, y_show=False)
    ))
fig1.show()
fig2.show()
fig3.show()
fig4.show()



# Grid and test function
# N = 29;
# x,y = np.linspace(-1,1, N*2), np.linspace(-1,1, N)
# X,Y = np.meshgrid(x,y)
F = lambda X,Y,Z : Ys_Ddoehlert+lambda_Ddoehlert[0]*X*X++lambda_Ddoehlert[1]*Y*Y++lambda_Ddoehlert[2]*Z*Z
# Z = F(X,Y)
# 3D Surface plot
print(lambda_Ddoehlert)
slice3d(F,[-1,1],[-1,1],0,"z")
slice3d(F,[-1,1],[-1,1],0,"y")
F = lambda X,Y,Z : Ys_Design3k+lambda_Design3k[0]*X*X++lambda_Design3k[1]*Y*Y++lambda_Design3k[2]*Z*Z
slice3d(F,[-1,1],[-1,1],0,"z")
F = lambda X,Y,Z : Ys_Dcomposite+lambda_Dcomposite[0]*X*X++lambda_Dcomposite[1]*Y*Y++lambda_Dcomposite[2]*Z*Z
slice3d(F,[-1,1],[-1,1],0,"z")

plt.show()
