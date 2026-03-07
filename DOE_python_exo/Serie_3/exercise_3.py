import os, sys, os.path, shutil
import matplotlib as mpl


mode_serv = False
for param in sys.argv[1:]:
    if param[:len("serv")]=="serv" and param[len("serv")] == "=":
        mode_serv = param[len("serv")+1:] in "1 y Y yes Yes YES"
#if not mode_serv:
#    mpl.use('TkAgg')
#else:
#    mpl.use('Agg')
if mode_serv:
    mpl.use('Agg')
try:
    import appnope
    appnope.nope()    # stop the apple power nap
except ImportError:
    pass

import pandas
from math import pi
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection
import numpy as np
from numpy.random import rand
from pylab import pcolor, show, colorbar, xticks, yticks, pcolormesh, imshow
from random import gauss
from scipy.interpolate import interp2d
import threading, multiprocessing, time
from decimal import Decimal
import scipy

from scipy.optimize import curve_fit
mpl.rc('text', usetex=True)
#plt.rc('text', usetex=True)
mpl.rc('text.latex',preamble=r"\usepackage{amsmath} \usepackage{graphicx} \usepackage{nicefrac} \usepackage{xcolor}")

import scipy as sp
import subprocess
import datetime
from matplotlib.ticker import PercentFormatter
from mpl_toolkits.mplot3d import Axes3D

from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import itertools
import sympy

def cov_to_sig_cor(cov, err=1e-100):
    std = np.sqrt(np.diag(cov))
    cor  = cov*1.
    cor /= (std[:, None]+err)
    cor /= (std[None, :]+err)
    return std, cor


c1=[0.04,0.04,0.04,0.04,0.05,0.06,0.06,0.06,0.06]
c2=[0.4, 0.4, 0.4, 0.8, 0.6, 0.4, 0.8, 0.8, 0.8]
c3=[-20, 0, 20, 0,0,0,-20,0,20]
c4=[[207.15, 206.74, 208.36],
    [206.45, 204.71, 206.83],
    [206.03, 203.22, 206.34],
    [194.51, 192.89, 195.03],
    [209.13, 209.09, 210.38],
    [222.86, 221.29, 222.08],
    [214.56, 212.06, 211.84],
    [209.52, 209.86, 211.35],
    [211.89, 210.2, 209.24]]


df = pandas.DataFrame(data={'C [%]': c1, 'S [%]': c2, 'T [C]': c3, 'E [kPa]': c4},)

print(df)


EXP_l=np.array([[ 1,-1,-1,-1],
              [ 1,-1,-1,0],
              [ 1,-1,-1,1],
              [ 1,-1,1,0],
              [ 1,0,0,0],
              [ 1,1,-1,0],
              [ 1,1,1,-1],
              [ 1,1,1,0],
              [ 1,1,1,1]])
     
EXP_int=np.array([[1,-1,-1,-1, 1],
                [1,-1,-1,0 , 1],
                [1,-1,-1,1 , 1],
                [1,-1,1,0  , -1],
                [1,0,0,0   , 0],
                [1,1,-1,0  , -1],
                [1,1,1,-1  , 1],
                [1,1,1,0   , 1],
                [1,1,1,1   , 1]])


d_lin= np.linalg.inv( (EXP_l.T@EXP_l))
d_int= np.linalg.inv( (EXP_int.T@EXP_int))

std_lin, corr_lin=cov_to_sig_cor(d_lin)
std_int, corr_int=cov_to_sig_cor(d_int)

VIF_lin=np.diag(np.linalg.inv(corr_lin))
VIF_int=np.diag(np.linalg.inv(corr_int))

C,S,T=sympy.symbols('C S T')
f_lin=np.array([1,C,S,T])
f_int=np.array([1,C,S,T,S*C])


Var_lin=f_lin.T.dot(d_lin.dot(f_lin).T)
Var_int=f_int.T.dot(d_int.dot(f_int).T)

print("#############")
print(Var_lin)
# Var_lin=Var_lin[0,0]
print(Var_lin)
print(Var_lin.subs(T,0))

print(EXP_l)
print(d_lin)
print(VIF_lin)
print(corr_lin)

# fig1=plt.figure(1)
# ax1=plt.subplot(111)
# ax1=sympy.plotting.plot3d(Var_lin.subs(T,0), (C, -1, 1), (S, -1, 1))



# Var_int=Var_int[0,0]
print(Var_int)
print(Var_int.subs(T,0))

print(EXP_int)
print(d_int)
print(VIF_int)
print(corr_int)

#ne marche plus
#c_lin=sp.stats.t.ppf((0.025, 0.975),df=5)[1]

sympy.plotting.plot3d(Var_lin.subs(T,0),Var_int.subs(T,0), (C, -1, 1), (S, -1, 1))

plt.show()