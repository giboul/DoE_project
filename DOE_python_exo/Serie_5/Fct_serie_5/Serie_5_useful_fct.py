import pandas #for dataframe
from math import pi
import math #always useful
import numpy as np #always useful (linear algebra expecially)
import scipy #for various mathematical function you may want
import statsmodels.api as sm #The most complete python pluggin 
#                             for statistical modeling in my sense
from statsmodels.formula.api import ols #For ordinary least square 
#                                       "ols" 
anova_lm = sm.stats.anova_lm #The anova function from statsmodels

# Documentation
# https://www.statsmodels.org/devel/regression.html
# https://www.statsmodels.org/devel/anova.html
# https://www.statsmodels.org/devel/examples/notebooks/generated/interactions_anova.html



#e.g. quadratic model 

c1=["H     ",    "t-C4H9    ",    "i-C3H7    ",    "C2H5      ",
    "CH3       ",    "CH2OH     ",    "C6H5      ",    "CH=CH2    ",
    "NH2       ",    "NHCH3     ",    "N(CH3)2   ",    "OH        ",
    "CO2C2H5   ",   "OCH3      ",    "Br        ",    "Cl        ", 
    "F         ",    "CN        ",    "NO2"]
c2=[0    ,    0    ,    0    ,    0    ,    0    ,    0.14 ,    0.1  ,
    0.06 ,    0.14 ,    0.12 ,    0.1  ,    0.3  ,    0.31 ,    0.28 ,
    0.45 ,    0.45 ,    0.44 ,    0.6  ,    0.65]
c3=[0,-0.07,-0.07,-0.07,-0.08,-0.06,-0.22,-0.15,-0.52,-0.58,-0.64,-0.38,
    0    ,-0.42,-0.15,-0.17,-0.25,0    ,0]
c4=[4390,4180,4060,3950,3850,3510,3350,3260,2600,2520,2250,2110,2020,
    1700,1290,1230,1060,1000,660]
# definition of a dataframe
df = pandas.DataFrame(data={'Amines': np.asarray(c1),
     'SigmaF': np.asarray(c2), 'SigmaR': np.asarray(c3),
     'K': np.asarray(c4)},)

mod_quad = ols('K ~ SigmaF*SigmaR + np.square(SigmaF) + np.square(SigmaR)', data=df)
res_quad=mod_quad.fit()# fitting of the model
print(res_quad.summary()) #returns the fitted model with : estimates, SE, 
                         # t-value, p-value, confidence interval, and
                         # various other statistical test and information
table_quad = anova_lm(res_quad, typ=2) #type II anova
print(table_quad)