import pandas as pd #for dataframe
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
import plotly.graph_objects as go # For isosurface and ternary plotting https://plotly.com/python/3d-isosurface-plots/



#Functions
#                     
import plotly.figure_factory as ff
terncontour=ff.create_ternary_contour        
from statsmodels.formula.api import ols #For ordinary least square "ols" 
from scipy.optimize import curve_fit # for various fit e.g linear fit
anova_lm = sm.stats.anova_lm #The anova function from statsmodels
incdf= scipy.stats.norm.ppf# inverse of the normal cumulative function 
eig=np.linalg.eig # compute a matrice eigen values and vectors
import plotly.express as px
ternplot=px.scatter_ternary #https://plotly.com/python/ternary-plots/
import plotly.figure_factory as ff
terncontour=ff.create_ternary_contour    # Equivalent of matlab ternarycontour https://plotly.com/python/ternary-contour/







def symplex(q,m): #idee codder simplement ligne par ligne
    Base=list(map(lambda k:k/m,range(m+1)))
    l_all=[list(p) for p in itertools.product(Base, repeat=q)]
    l_symp=[]
    for l in l_all:
        if sum(l)==1: l_symp+=[l]
    return np.array(l_symp[::-1])
print(symplex(4,3))    
symp=symplex(4,3)

df=pd.DataFrame(data=symp,columns=["c1","c2","c3","c4"])
fig1 = ternplot(df[9:], a="c2", b="c3", c="c4",size_max=15)
fig2 = ternplot(df[4:9], a="c2", b="c3", c="c4")
fig3 = ternplot(df[1:4], a="c2", b="c3", c="c4")


symp=symplex(3,5)
print(symp)
df=pd.DataFrame(data=symp,columns=["c2","c3","c4"])
fig4 = ternplot(df, a="c2", b="c3", c="c4",size_max=15)

fig1.show()
fig2.show()
fig3.show()
fig4.show()

#P2
symp=np.array([[0   ,0   ,1  ],
      [0   ,1   ,0  ],
      [1   ,0   ,0  ],
      [0.5 ,0.5 ,0  ],
      [0.5 ,0   ,0.5],
      [0   ,0.5 ,0.5]])




print(symp)
Y1=np.array([1,1.2,1.3,3,3.4,3.6])
df=pd.DataFrame(data=np.c_[Y1,symp],columns=["c0","c1","c2","c3"])
print(df)
model=ols("c0 ~ c1*c2*c3 - c1:c2:c3 -1",data=df)
mdl_fit=model.fit()
print(mdl_fit.summary())


symp=np.array([[0   ,0   ,1  ],
               [0   ,1   ,0  ],
               [1   ,0   ,0  ],
               [0.5 ,0.5 ,0  ],
               [0.5 ,0   ,0.5],
               [0   ,0.5 ,0.5],
               [0   ,0   ,1  ],
               [0   ,1   ,0  ],
               [1   ,0   ,0  ],
               [0.5 ,0.5 ,0  ],
               [0.5 ,0   ,0.5],
               [0   ,0.5 ,0.5]])

print(symp)
Y1=np.array([1,1.2,1.3,3,3.4,3.6,1.1,1.4,1.4,3.2,3.3,3.7])
df=pd.DataFrame(data=np.c_[Y1,symp],columns=["c0","c1","c2","c3"])
print(df)
model=ols("c0 ~ c1*c2*c3 - c1:c2:c3 -1",data=df)
mdl_fit=model.fit()
print(mdl_fit.summary())


fig5 = terncontour(symp.T, Y1,pole_labels=['c1', 'c2', 'c3'],
                                interp_mode='cartesian')
fig5.show()






