import pandas as pd                                   # importing pandas for dataframe
from matplotlib import pyplot as plt                  # importing for EDA 
df = pd.read_csv("OnlineRetail.csv")                  # importing online retal file          
df



df.dtypes                                               # checking datatypes for each features

# Q1)   performing typecasting

df["UnitPrice"] = df["UnitPrice"].astype("int64")       # converting float to int
df
df.UnitPrice

df["Quantity"] = df["Quantity"].astype("float64")       # converting int to float
df
df.Quantity  

# Q2)  Checking for duplicate values

duplicate = df.duplicated()                            # checking for duplicates
duplicate                                              # printing duplicates
sum(duplicate)                                         # taking sum of rows having duplicates
df1 = df.drop_duplicates()                             # dropping duplicate values
df1
#  Q3) EDA
#  for quantity feature

df1.Quantity.describe()
plt.hist(df1.Quantity)
plt.boxplot(df1.Quantity)

# for unitprice feature

df1.UnitPrice.describe()
plt.hist(df1.UnitPrice)
plt.boxplot(df1.UnitPrice)

# scatter plot

plt.scatter(df1.UnitPrice,df1.Quantity)
