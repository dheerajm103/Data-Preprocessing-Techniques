import pandas as pd                                      # importing libraries
import numpy as np                                   
import scipy.stats as stats
import pylab
df = pd.read_csv("calories_consumed.csv")                # importing dataset
df

# using log transformation

stats.probplot(df.Weight,dist="norm",plot=pylab)        # plotting QQ plot for Weight
weight = np.log10(df.Weight)                            # transforming weight to log 
weight
stats.probplot(weight,dist="norm",plot=pylab)           # plotting QQ plot fortransformed weight 

stats.probplot(df.Calories,dist="norm",plot=pylab)      # plotting QQ plot for calories
calories = np.log10(df.Calories)                        # transforming calories to log 
calories
stats.probplot(calories,dist="norm",plot=pylab)         # plotting QQ plot fortransformed calories

# using squareroot transformation

stats.probplot(df.Weight,dist="norm",plot=pylab)        # plotting QQ plot for Weight
weight1 = np.sqrt(df.Weight)                            # transforming weight to square root
weight1 
stats.probplot(weight1,dist="norm",plot=pylab)          # plotting QQ plot fortransformed weight

stats.probplot(df.Calories,dist="norm",plot=pylab)      # plotting QQ plot for calories
calories1 = np.sqrt(df.Calories)                        # transforming calories to square root
calories1
stats.probplot(calories1,dist="norm",plot=pylab)        # plotting QQ plot fortransformed calories

# using resiprocal transformation

stats.probplot(df.Weight,dist="norm",plot=pylab)        # plotting QQ plot for Weight  
weight2 = np.reciprocal(df.Weight)                      # transforming weight to reciprocal                    
weight2
stats.probplot(weight2,dist="norm",plot=pylab)          # plotting QQ plot fortransformed weight

stats.probplot(df.Calories,dist="norm",plot=pylab)      # plotting QQ plot for calories
calories2 = np.reciprocal(df.Calories)                  # transforming calories to deciprocal             
calories2
stats.probplot(calories2,dist="norm",plot=pylab)        # plotting QQ plot fortransformed calories
