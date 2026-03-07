import numpy as np #always useful (linear algebra expecially and sampling)

#In: the order of the model
#Out: the doehlert matrix
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
    
