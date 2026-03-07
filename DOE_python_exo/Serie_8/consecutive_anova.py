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
# from Wilkinson import *
#Functions
#                             
from statsmodels.formula.api import ols #For ordinary least square "ols" 
from scipy.optimize import curve_fit # for various fit e.g linear fit
anova_lm = sm.stats.anova_lm #The anova function from statsmodels

#In: The model, the data frame as for the OLS function, the max p_value of the parameters (0.05 by default)
#Out: The final anova table, the final model fit result
#Description: Performs consecutive anova, removing at each step the parameter with the biggest p_value (if above the max value)
def consecutive_anova(mdl,data,pvalue=0.05,print_step=False):
    mod=ols(mdl,data=data)
    fit_model=mod.fit()
    if any(np.isinf(fit_model.bse)):
        print("Error: Too many parameter to fit for the data size")
        print("Anova impossible -> exit")
        exit()
    T_anova=anova_lm(fit_model,typ=2)
    if print_step:print(T_anova)
    max_p=0.
    id_mp=0
    for i in range(len(T_anova["PR(>F)"])):
        if T_anova["PR(>F)"][i]>max_p: 
            max_p=T_anova["PR(>F)"][i]
            id_mp=i
    if max_p>pvalue:
        new_mdl=mdl+" -"+str(T_anova.index.values[id_mp])
        # print(new_mdl)
        return consecutive_anova(new_mdl,data,pvalue,print_step)
    else:
        return T_anova, fit_model