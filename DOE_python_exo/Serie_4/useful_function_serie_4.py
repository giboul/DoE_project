import os, sys, os.path, shutil # alway nice typically for file reading
import xlrd, openpyxl   # same with excel file
import matplotlib as mpl #for figure and 3s figure
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

def renorm(a): # just renormalize the vector a between -1 and 1
 v=a.to_numpy()
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