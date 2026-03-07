import pandas as pd#for dataframe
from math import pi
import math #always useful
import matplotlib as mpl # for plot
import matplotlib.pyplot as plt # for plot
import numpy as np #always useful (linear algebra expecially and sampling)
import scipy #for various mathematical function you may want and hadamard matrices
import statsmodels.api as sm #The most complete python package for statistical modeling in my sense
import pyDOE # Warning lot of compatibility problem (useless in 2022 but may corrected in the future)
import itertools
import sympy
from mesure3 import *
import plotly.graph_objects as go # For isosurface plotting https://plotly.com/python/3d-isosurface-plots/



#Functions
#                             
from statsmodels.formula.api import ols #For ordinary least square "ols" 
from scipy.optimize import curve_fit # for various fit e.g linear fit
anova_lm = sm.stats.anova_lm #The anova function from statsmodels
incdf= scipy.stats.norm.ppf# inverse of the normal cumulative function 
eig=np.linalg.eig # compute a matrice eigen values and vectors