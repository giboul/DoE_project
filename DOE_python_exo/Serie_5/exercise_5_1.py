import os, sys, os.path, shutil # alway nice typically for file reading
import xlrd, openpyxl   # same with excel file
import matplotlib as mpl #for figure and 3s figure
import matplotlib.pyplot as plt #for figure and 3s figure
from matplotlib.ticker import PercentFormatter 
from mpl_toolkits.mplot3d import Axes3D #3d plot
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import pweave #for pdf production
import pandas #for dataframe
from math import pi
import math #always useful
import numpy as np #always useful (linear algebra expecially)
import scipy #for various mathematical function you may want
import itertools # to produce sample out of list if necessary
import sympy # for symbolic variable calculation equivalent to the sym declaration in matlab
import sklearn as sk # for generalized linear model
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
import statsmodels.api as sm #For ordinary least square "sm.OLS" 
from statsmodels.formula.api import ols #For ordinary least square "ols" not the same as above 



# https://www.statsmodels.org/devel/regression.html
# https://www.statsmodels.org/devel/anova.html
# https://www.statsmodels.org/devel/examples/notebooks/generated/interactions_anova.html

def renorm(a): # just renormalize the vector a between -1 and 1
 # print("type")
 # print(a.dtype)
 v=np.asarray(a)
 # print(v)
 s=[]
 min_v=np.amin(v)
 max_v=np.amax(v)
 dif=max_v-min_v
 for val in v:
     s+=[(val-min_v)/dif*2-1]
 return s

# In : The experiment matrix (format: numpy matrix), the number of rows to be reduced to (the final number of experiment wanted, and the maximum number of iteration (800 by default)
# Out: "D-optimale information matrix"  and information matrix determinant
# principle: a replacemnt for matlab candexch function, iterative procedure, do not sort the rows automatically 
def candexch(C,nrows,n_try=800): 
    rows=range(len(C))
    opti_mat=[]
    start_id=np.random.choice(len(C),size=nrows,replace=True)
    start_point=[C.tolist()[i] for i in start_id]
    # print("start_point",start_point)
    X=np.mat(start_point)
    ref_det=np.linalg.det(np.matmul(X.T,X))
    det=0
    max_det=0
    opti_mat1=np.zeros(X.shape)
    opti_mat_old=np.zeros(X.shape)
    opti_mat2=X
    itera=0
    while((not np.array_equal(opti_mat_old,opti_mat2)) and (itera<n_try)):
        opti_mat_old=opti_mat2
        min_dif_det=math.inf
        det=0
        max_det=0
        for row in C:
            X=np.vstack([opti_mat2,row])
            # print(X)
            det=np.linalg.det(np.matmul(X.T,X))
            if abs(det) > max_det:
                max_det=abs(det)
                opti_mat1=X
        # print(opti_mat1)
        for i in range(len(opti_mat1)):
            X=np.delete(opti_mat1,i,axis=0)
            # print(X)
            det=np.linalg.det(np.matmul(X.T,X))
            if abs(max_det-det) < min_dif_det:
                min_dif_det=abs(max_det-det)
                opti_mat2=X
        itera +=1
        # print(itera)
        # print(opti_mat2)
    print("number of iter",itera)
    return opti_mat2, max_det

c1=["H     ",    "t-C4H9    ",    "i-C3H7    ",    "C2H5      ",    "CH3       ",    "CH2OH     ",    "C6H5      ",    "CH=CH2    ",    "NH2       ",    "NHCH3     ",    "N(CH3)2   ",    "OH        ",    "CO2C2H5   ",   "OCH3      ",    "Br        ",    "Cl        ",   "F         ",    "CN        ",    "NO2"]
c2=[0    ,    0    ,    0    ,    0    ,    0    ,    0.14 ,    0.1  ,    0.06 ,    0.14 ,    0.12 ,    0.1  ,    0.3  ,    0.31 ,    0.28 ,    0.45 ,    0.45 ,    0.44 ,    0.6  ,    0.65]
c3=[0,-0.07,-0.07,-0.07,-0.08,-0.06,-0.22,-0.15,-0.52,-0.58,-0.64,-0.38,0    ,-0.42,-0.15,-0.17,-0.25,0    ,0]
c4=[4390,4180,4060,3950,3850,3510,3350,3260,2600,2520,2250,2110,2020,1700,1290,1230,1060,1000,660]


df = pandas.DataFrame(data={'Amines': np.asarray(c1), 'SigmaF': np.asarray(c2), 'SigmaR': np.asarray(c3), 'K': np.asarray(c4)},)

print(df)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter3D(df["SigmaF"],df["SigmaR"],df["K"])
ax.set_xlabel("$\sigma_F$")
ax.set_ylabel("$\sigma_R$")
ax.set_zlabel("K")
# print(df["SigmaF"].dtype)    

#not normalized
X_lin=np.mat((np.ones(len(df["SigmaF"])),(df["SigmaF"]),(df["SigmaR"]))).T
print(X_lin)
X_int=np.mat((np.ones(len(df["SigmaF"])),(df["SigmaF"]),(df["SigmaR"]),np.multiply((df["SigmaF"]),(df["SigmaR"])))).T
print(X_int)
X_quad=np.mat((np.ones(len(df["SigmaF"])),(df["SigmaF"]),(df["SigmaR"]),np.multiply((df["SigmaF"]),(df["SigmaR"])),np.power((df["SigmaF"]),2),np.power((df["SigmaR"]),2))).T
print(X_quad)
# X_lin=np.mat((np.ones(len(df["SigmaF"])),renorm(df["SigmaF"]),renorm(df["SigmaR"]))).T
# print(X_lin)
# X_int=np.mat((np.ones(len(df["SigmaF"])),renorm(df["SigmaF"]),renorm(df["SigmaR"]),np.multiply(renorm(df["SigmaF"]),renorm(df["SigmaR"])))).T
# print(X_int)
# X_quad=np.mat((np.ones(len(df["SigmaF"])),renorm(df["SigmaF"]),renorm(df["SigmaR"]),np.multiply(renorm(df["SigmaF"]),renorm(df["SigmaR"])),np.power(renorm(df["SigmaF"]),2),np.power(renorm(df["SigmaR"]),2))).T
# print(X_quad)
# X_quad2=np.mat((np.ones(len(df["SigmaF"])),renorm(np.power(df["SigmaF"],2)),renorm(np.power(df["SigmaR"],2)))).T
# print(X_quad2)


d_lin= np.linalg.inv( np.matmul(X_lin.T,X_lin))

d_int= np.linalg.inv( np.matmul(X_int.T,X_int))

d_quad= np.linalg.inv( np.matmul(X_quad.T,X_quad))

print(d_lin)
print(d_int)
print(d_quad)


Y=np.mat(df["K"]).T
print(Y)
Coef_lin=np.matmul(d_lin,np.matmul(X_lin.T,Y)).T
print(Coef_lin)
Coef_int=np.matmul(d_int,np.matmul(X_int.T,Y)).T
print(Coef_int)
Coef_quad=np.matmul(d_quad,np.matmul(X_quad.T,Y)).T
print(Coef_quad)

reg_lin= linear_model.LinearRegression()
reg_lin.fit(X_lin[:,1:],Y)
print(reg_lin.coef_)
print(reg_lin.intercept_)


Y=np.array(Y.T.tolist()[0])


model = Pipeline([('quad', PolynomialFeatures(degree=2)), ('inter', PolynomialFeatures(degree=2,interaction_only=True))])
# fit to an order-3 polynomial data
model = model.fit(X_lin[:,1:], Y)
print(model.named_steps['quad'].powers_)

# print(Y.T.tolist()[0])
# V=scipy.optimize.lsq_linear(X_lin,Y.T)
# print(V)
# V=scipy.optimize.lsq_linear(X_quad,Y.T)
# print(V)
# V=scipy.optimize.lsq_linear(X_int,Y.T)
# print(V)



# df_norm = pandas.DataFrame(data={'Amines': c1, 'SigmaF': renorm(c2), 'SigmaR': renorm(c3), 'K': c4},)

print(df)

res_lin = ols("K ~ SigmaF + SigmaR", df).fit()
# res_lin=mod_lin.fit()
print(res_lin.summary())
table_lin = sm.stats.anova_lm(res_lin, typ=2)
print(table_lin)

mod_int = ols('K ~ SigmaF*SigmaR', data=df)
res_int=mod_int.fit()
print(res_int.summary())
table_int = sm.stats.anova_lm(res_int, typ=2)
print(table_int)


mod_quad = ols('K ~ SigmaF*SigmaR + np.power(SigmaF,2) + np.power(SigmaR,2)', data=df)
res_quad=mod_quad.fit()
print(res_quad.summary())
table_quad = sm.stats.anova_lm(res_quad, typ=2)
print(table_quad)

mod_quad2 = ols('K ~ SigmaF + np.power(SigmaF,2) ', data=df)
res_quad2=mod_quad2.fit()
print(res_quad2.summary())
table_quad2 = sm.stats.anova_lm(res_quad2, typ=2)
print(table_quad2)


