
import pandas as pd                                       # importing libraries
import numpy as np
import scipy.stats as stats
from sklearn import preprocessing
import pylab
df                          # importing dataset
df
df.describe()

# using standardisation for scale  and unit free

scaler = preprocessing.StandardScaler()                   # initialising standard scaler
df1 = scaler.fit_transform(df)                            # transforming the data set
df2 = pd.DataFrame(df1)                                   # converting transformed dataset to dataframe
df2

df2.describe()
stats.probplot(df3.Area,dist="norm",plot=pylab)  
# using normalisation for scale  and unit free
                  
def norm(i):                                              # creating function for normalisation
    x= (i - i.min())/ (i.max()- i.min())
    return x
df3 = norm(df)                                           # passing dataset for normalisation
df3
