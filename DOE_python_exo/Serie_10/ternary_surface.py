#derived from https://stackoverflow.com/questions/57483209/how-do-i-highlight-a-slice-on-a-matplotlib-3d-surface-plot
#Warning the surfaace is drawn in a cartesian environment by necessity

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

#In :The values on the coordinates matrix X (N x 3) and Z the results (N x 1)
#Out the ternary suface (in a cartesian environment)
#    Warning use the same order as in slide 6.3.2 transformation ternary to catesian
def ternary_surface(X,Z):
    pass_mat=np.array([[1,0.5,0],
                       [0,np.sqrt(3)/2,0],
                       [1,1,1]])
    val=np.array(list(map(lambda x: pass_mat.dot(x),X)))
    # F_mat=
    X=val[:,0]
    Y=val[:,1]
    val=np.c_[val,Z]
    print(val)
    # X1,Y1=np.meshgrid(X,Y)
    # Zt=np.empty(X.shape)
    # Zt[:]=np.nan
    # print(X)
    # print(Y)
    # for i in range(len(X)):
        # for j in range(len(X[0])):
            # for k in range(len(val)):
                # if X[i,j]==val[k,0] and Y[i,j]==val[k,1]:
                    # Zt[i,j]=val[k,3]
    # print(Zt)
    # 3D Surface plot
    plt.figure(figsize = (5,6))
    ax = plt.subplot(111, projection='3d')
    # Normalise Y for calling in the cmap.
    # Zs = Zt/Zt.max()
    cmap = plt.cm.viridis
    ax.plot_trisurf(X, Y, Z, cmap=plt.cm.viridis, antialiased=True)
    
    
    
symp=np.array([[0   ,0   ,1  ],
      [0   ,1   ,0  ],
      [1   ,0   ,0  ],
      [0.5 ,0.5 ,0  ],
      [0.5 ,0   ,0.5],
      [0   ,0.5 ,0.5]])


Y1=np.array([1,1.2,1.3,3,3.4,3.6])

ternary_surface(symp,Y1)

plt.show()