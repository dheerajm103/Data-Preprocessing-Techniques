import pandas as pd                                            # importing libraries
from sklearn import preprocessing
df = pd.read_csv("animal_category.csv")                        # importing data set
df



df.drop(['Index'], axis=1, inplace=True)                            # dropping index feature which is nominal
df

# creating dummy variable

df1 = pd.get_dummies(df)
df1
df2 = pd.get_dummies(df, drop_first = True)                         # droping first column
df2

# creating dummy variable by one hot encoding

ohe = preprocessing.OneHotEncoder()                                 # initialising
df3 = pd.DataFrame(ohe.fit_transform(df.iloc[:, :]).toarray())      # transforming
df3

# creating dummy variable by label encoder

ln = preprocessing.LabelEncoder()                                   # initialising 
df["Animals"] = ln.fit_transform(df["Animals"])                     # transforming to animal feature
df["Gender"] = ln.fit_transform(df["Gender"])                       # transforming to gender feature
df["Homly"] = ln.fit_transform(df["Homly"])                         # transforming to homly feature
df["Types"] = ln.fit_transform(df["Types"])                         # transforming to types feature
df
