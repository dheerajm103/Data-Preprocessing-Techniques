import pandas as pd                         # Importing libraries
import numpy as np
from sklearn.impute import SimpleImputer
df = pd.read_csv("claimants.csv")          # importing dataset
df


df.isna().sum()                           # checking for missing values in dataset

# importing mode imputer for features CLMSEX,CLMINSUR,SEATBELT

mode_imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')

# Filling nan values with fit_transformation

df["CLMINSUR"] = pd.DataFrame(mode_imputer.fit_transform(df[["CLMINSUR"]]))
df["SEATBELT"] = pd.DataFrame(mode_imputer.fit_transform(df[["SEATBELT"]]))
df["CLMSEX"] = pd.DataFrame(mode_imputer.fit_transform(df[["CLMSEX"]])) 

# Importing median imputer for feature CLMAGE

median_imputer = SimpleImputer(missing_values=np.nan, strategy='median')

# Filling nan values with fit_transformation

df["CLMAGE"] = pd.DataFrame(median_imputer.fit_transform(df[["CLMAGE"]]))


df.isna().sum()                         # checking missing values for dataset
df
