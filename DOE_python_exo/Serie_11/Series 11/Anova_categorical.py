import statsmodels.api as sm #The most complete python package for statistical modeling in my sense
import pandas as pd #for dataframe
from statsmodels.formula.api import ols #For ordinary least square "ols" 
from scipy.optimize import curve_fit # for various fit e.g linear fit
anova_lm = sm.stats.anova_lm #The anova function from statsmodels


#Exemple of fit for categorical variable
#It uses a standard way of displaying the results, the fist category is considered as 
# a reference and is implicitly added to the constant. The effects are actually the contrast with the 
# reference variable. It is done so because the actual degree of freedom of a variable with N category is
# N-1 
Cat=['A']*4+['B']*4+['C']*4+['D']*4+['E']*4
# Cat=np.array([1]*4+[2]*4+[3]*4+[4]*4+[5]*4)
val=[1,3,5,3,9,5,5,5,6,6,3,3,3,3,0,6,14,10,18,14]

df=pd.DataFrame(data={"Values":val,"Treatments":Cat})
df=df[['Values','Treatments']].dropna()
print(df['Treatments'].dtypes)
print(Cat)
model=ols(formula='Values ~ Treatments',data=df)
mdl_fit=model.fit()
print(mdl_fit.summary())
#prints the anova per VARIABLE, to have per category you need to redefine your model
#with one variable for each category
print(anova_lm(mdl_fit))