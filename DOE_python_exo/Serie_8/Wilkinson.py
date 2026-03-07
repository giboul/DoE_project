

# In: A list of variable name (the dependant variable should the first one) 
#     and a model ("linear","interactions","quadratic")
# Out: The Wilkinson formulation of the model for the OLS function
def Wilkinson(cols,model="linear"):
   formula=cols[0] + " ~" 
   if model=="linear":
       for col in cols[1:]:
           formula+= " + "+col
   elif model=="interactions":
       formula+= " "+cols[1]
       for col in cols[2:]:
           formula+= "*"+col
   elif model=="quadratic":
       formula+= " "+cols[1]
       for col in cols[2:]:
           formula+= "*"+col
       for col in cols[1:]:
           formula+= " + np.power("+col+",2)"
   else:
       print("Error in Wilkinson Unknown model in input")
       exit()
   return formula
   
   
#Example: interactions model 4 variables + the dependrent one
W=Wilkinson(["c0","c1","c2","c3","c4"],"interactions")
print(W)