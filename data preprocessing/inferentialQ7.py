import pandas as pd  # importing modules
import matplotlib
from matplotlib import pyplot as plt
%matplotlib inline
import numpy as np
import scipy.stats as stats
import pylab

df = pd.read_csv("inferentialQ.csv")  # importing dataset
df

df.describe()  # calculating mean,median,sd,

df.var()     #    calculating variance

df.mode()    #    calculating mode

plt.boxplot(df.po) # ploting boxplot

stats.probplot(df.po , dist="norm", plot=pylab) # ploting normal distribution

plt.hist(df.po) # ploting histogram
