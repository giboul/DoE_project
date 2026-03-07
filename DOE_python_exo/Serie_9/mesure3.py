import numpy as np #always useful (linear algebra expecially and sampling)
import scipy #for various mathematical function you may want and hadamard matrices



def mesure3(X):
    # Y=mesure3(X)
    # Renvoie les mesures correspondant aux points 3D contenus dans X
    
    #  l'écart-type s vaut 1/10
    s=0.01 # variance
    
    x1=X[:,0]
    x2=X[:,1]
    x3=X[:,2]
    return np.multiply(np.exp(-2* (np.power(x1,2)/3+np.power(x2,2)/2) ),np.exp(x1-x2))+0.5*x3 +s*np.random.randn(len(x1))
