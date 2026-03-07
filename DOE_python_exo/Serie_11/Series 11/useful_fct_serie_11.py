import pandas as pd #for dataframe
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
import plotly.graph_objects as go # For isosurface and ternary plotting https://plotly.com/python/3d-isosurface-plots/



#Functions
#                     
from statsmodels.formula.api import ols #For ordinary least square "ols" 
from scipy.optimize import curve_fit # for various fit e.g linear fit
anova_lm = sm.stats.anova_lm #The anova function from statsmodels


#Exemple Dotplot
import plotly.express as px
df = px.data.medals_long()

fig = px.scatter(df, y="nation", x="count", color="medal", symbol="medal")
fig.update_traces(marker_size=10)
fig.show()

#Exemple anova
