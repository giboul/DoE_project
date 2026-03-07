from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

#In: the function, the limits of x1,x2 axis, the height on the last axis, and the axis perpendicaular to the slice
#out: plot of the slice in a 3d environement.
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
    cmap = plt.cm.plasma
    # vs=np.sqrt((vs-vs.min())/abs(vs-vs.min()).max())*2-1
    vs=(vs-vs.min())/abs(vs-vs.min()).max()
    # vs=np.log10(abs(vs))/np.log(abs(vs)).max()
    if const_axis=="z":  surf=ax.plot_surface(X1, X2, X3, facecolors=cmap(vs),
                       linewidth=0, antialiased=False)
    elif const_axis=="y":surf=ax.plot_surface(X1, X3, X2, facecolors=cmap(vs),
                       linewidth=0, antialiased=False)
    elif const_axis=="x":surf=ax.plot_surface(X3, X1, X2, facecolors=cmap(vs),
                       linewidth=0, antialiased=False)





#example 
F= lambda X,Y,Z : np.sqrt(X*X+Y*Y+Z*Z) 
slice3d(F,[-1,1],[-1,1],0,"z")
plt.show()





