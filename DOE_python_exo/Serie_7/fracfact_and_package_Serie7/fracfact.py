import pandas #for dataframe
from math import pi
import math #always useful
import matplotlib as mpl # for plot
import matplotlib.pyplot as plt # for plot
import numpy as np #always useful (linear algebra expecially and sampling)
import scipy #for various mathematical function you may want and hadamard matrices
import statsmodels.api as sm #The most complete python package for statistical modeling in my sense
import pyDOE # Warning lot of compatibility problem (useless in 2022 but may corrected in the future)
import itertools
#Functions
#                             

#In: An arry with the generator, see exymple bellow 
#Out: The Essay matrix
#     The table of alias
#Summary: Create the fractional factorial model from the generator similarly to the matlab exemple in the course
#         Only two level and maxInt mod

def fracfact(ini_gen):
    def ff2n(order):
        mat=[]
        for i in range(order):
            tmp=[-1]*int(np.power(2,order-i-1))+[1]*int(np.power(2,order-i-1))
            mat+=[tmp*int(np.power(2,i))]
        return np.array(mat).T
    gen=ini_gen
    mult_col=[]
    for i in range(len(gen)):
        col=[]
        for j in range(len(gen)):
            if (gen[j] in gen[i]) and(len(gen[j])==1): col += [j]
        mult_col += [col]
    order=0
    for i in mult_col:
        if len(i)==1: order +=1
    full=ff2n(order)
    frac=np.ones((len(gen),len(full)))
    id_=0
    for i in mult_col:
        if len(i)==1: 
            frac[i[0]]=full.T[id_]
            id_+=1
    frac=frac.T
    for i in range(len(frac)):
        for j in range(len(mult_col)):
            if len(mult_col[j])!=1:
                for k in mult_col[j]:
                    frac[i][j]*=frac[i][k]
    Term_=["X"+str(1+i) for i in range(len(gen))]
    Term=Term_
    generator_=gen
    for i in range(len(Term_)):
        for j in range(len(Term_)):
            Term += [Term_[i]+"*"+Term_[j]]
            generator_ +=[gen[i]+gen[j]]
    generator=[]
    Term =[t.split("*") for t in Term] 
    Term =[sorted(t) for t in Term] 
    Term =sorted(Term,key=len)
    def rewrite(arr):
       s=arr[0]
       for i in range(1,len(arr)):
           s+=("*"+arr[i])
       return s
    def genname(arr):
        s=[]
        if(len(arr)>1):
            for i in arr:
                print(Term_.index(i))
                s+=ini_gen[Term_.index(i)]
            return s
        else:
            return ini_gen[Term_.index(arr[0])]
    generator_=[genname(t) for t in Term]
    Term = [rewrite(t) for t in Term]
        
    for s in generator_:
        dico={}
        for t in s :
           if not t in dico : dico.update({t:1})
           else: dico[t] +=1
        new_s=""
        for t in s:
            if ((t not in new_s ) and (np.mod(dico[t],2)==1)):
               new_s += t
        if not new_s: new_s="I"
        generator+=["".join(sorted(new_s))]
    check=[]
    to_del=[]
    for i in range(len(generator)):
        if generator[i]=="I" or generator[i] in check:
            to_del+=[i]
        else:
            check+=[generator[i]]
    Term2=np.delete(Term,to_del)
    generator2=np.delete(generator,to_del)
    Table=[Term2]+[generator2]
    return frac, np.asarray(Table).T
    
#same exemples in the course slides
test, table= fracfact(["bcde","b","c","d","e"])
# test, table= fracfact(["a","b","c","ab","abc"])
print(test)
print(table)