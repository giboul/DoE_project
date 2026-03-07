#derived from https://stackoverflow.com/questions/57483209/how-do-i-highlight-a-slice-on-a-matplotlib-3d-surface-plot
#Warning the surfaace is drawn in a cartesian environment by necessity

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Grid and test function
N = 29;
x,y = np.linspace(-1,1, N*2), np.linspace(-1,1, N)
X,Y = np.meshgrid(x,y)
F = lambda X,Y : np.sin(10*X)/(1+5*(X**2+Y**2))
Z = F(X,Y)
#In :The values on the coordinates matrix X (N x 3) and Z the results (N x 1)
#Out the ternary suface (in a cartesian environment)
#    Warning use the same order as in slide 6.3.2 transformation ternary to catesian
def ternary_surface(X,Z)
    pass_mat=np.array([[1,0.5,0],
                       [0,np.sqrt(3)/2,0],
                       [1,1,1]])
    val=np.array(map(lambda x: pass_mat.dot(x),X))
    X=val[:,0]
    Y=val[:,1]
    # 3D Surface plot
    plt.figure(figsize = (5,6))
    ax = plt.subplot(211, projection='3d')
    # Normalise Y for calling in the cmap.
    Zs = Z/Z.max()
    cmap = plt.cm.viridis
    ax.plot_surface(X, Y, Z, facecolors=cmap(Ys))
    
    # 2D Plot of slice of 3D plot 
    Normalise y for calling in the cmap.
    # ys = y/y.max()
    # plt.subplot(212)
    # plt.plot(x,Z[10,:], color=cmap(ys[10]))
    # plt.plot(x,Z[20,:], color=cmap(ys[20]))
    # plt.show()
    
    # plt.savefig('surfacePlotHighlight.png')
    
    
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

Y1=np.array([1,1.2,1.3,3,3.4,3.6,1.1,1.4,1.4,3.2,3.3,3.7])
ternary_surface(symp,Y1)

plt.show()