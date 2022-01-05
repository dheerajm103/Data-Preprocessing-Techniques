import pandas as pd                                # importing libraries
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from feature_engine.outliers import Winsorizer

df = pd.read_csv("bostondata.csv")                 # importing dataset
df

# checking outliers for crim feature ********************************************

sns.boxplot(df.crim)                               # using box plot outliers detected   

Q1 = df.crim.quantile(0.25)                        # calculating lower quartile
Q1
Q3 = df.crim.quantile(0.75)                        # calculating upper quartile
Q3
IQR = Q3 - Q1                                      # calculating IQR
IQR
upper_limit = df.crim.quantile(0.75) +1.5*IQR      # calculating upper limit 
upper_limit

lower_limit = df.crim.quantile(0.25) -1.5*IQR      # calculating lower limit
lower_limit
# detecting outliers in terms of true

outliers_df = np.where((df.crim > upper_limit), True, np.where(df.crim< lower_limit, True, False))
outliers_df
df_trimmed = df.loc[~(outliers_df), ]             # trimming  the outliers
df_trimmed

df.shape,df_trimmed.shape                         # shape of original dataframe and trimmed dataframe
sns.boxplot(df_trimmed.crim)                              # checking outliers in trimmed dataframe

# replacing outliers to their upper limit and lower limit respectively

df['df_replaced'] = pd.DataFrame(np.where(df['crim'] > upper_limit, upper_limit, np.where(df['crim'] < lower_limit, lower_limit, df['crim'])))

plt.boxplot(df.df_replaced)                        # checking outliers in replaced dataframe

# replacing outliers using winsorization

# initialising winsorizer with iqr as capping method fold up to 1.5
winsor = Winsorizer(capping_method='iqr',tail='both',fold=1.5,variables=['crim'])

df_t = winsor.fit_transform(df[['crim']])          # transforming for replacing outliers         
sns.boxplot(df_t.crim)                             # checking for outliers  


# checking outliers for zn feature ************************************************

sns.boxplot(df.zn)                                 # checking outliers for zn           

Q1 = df.zn.quantile(0.25)                        # calculating lower quartile
Q1
Q3 = df.zn.quantile(0.75)                        # calculating upper quartile
Q3
IQR = Q3 - Q1                                      # calculating IQR
IQR
upper_limit = df.zn.quantile(0.75) +1.5*IQR      # calculating upper limit 
upper_limit

lower_limit = df.zn.quantile(0.25) -1.5*IQR      # calculating lower limit
lower_limit
# detecting outliers in terms of true

outliers_df = np.where((df.zn > upper_limit), True, np.where(df.zn< lower_limit, True, False))
outliers_df
df_trimmed = df.loc[~(outliers_df), ]             # trimming  the outliers
df_trimmed

df.shape,df_trimmed.shape                         # shape of original dataframe and trimmed dataframe
sns.boxplot(df_trimmed.zn)                        # checking outliers in trimmed dataframe

# replacing outliers to their upper limit and lower limit respectively

df['df_replaced'] = pd.DataFrame(np.where(df['zn'] > upper_limit, upper_limit, np.where(df['zn'] < lower_limit, lower_limit, df['zn'])))

plt.boxplot(df.df_replaced)                       # checking outliers in replaced dataframe

# replacing outliers using winsorization

# initialising winsorizer with iqr as capping method fold up to 1.5
winsor = Winsorizer(capping_method='iqr',tail='both',fold=1.5,variables=['zn'])

df_t = winsor.fit_transform(df[['zn']])          # transforming for replacing outliers         
sns.boxplot(df_t.zn)                             # checking for outliers  


# checking outliers for indus feature*********************************************

sns.boxplot(df.indus)                           # no outlier detected


# checking outlier for chas feature **********************************************

sns.boxplot(df.chas)                            # checking for outlier 

Q1 = df.chas.quantile(0.25)                        # calculating lower quartile
Q1
Q3 = df.chas.quantile(0.75)                        # calculating upper quartile
Q3
IQR = Q3 - Q1                                      # calculating IQR
IQR
upper_limit = df.chas.quantile(0.75) +1.5*IQR      # calculating upper limit 
upper_limit

lower_limit = df.chas.quantile(0.25) -1.5*IQR      # calculating lower limit
lower_limit
# detecting outliers in terms of true

outliers_df = np.where((df.chas > upper_limit), True, np.where(df.chas< lower_limit, True, False))
outliers_df
df_trimmed = df.loc[~(outliers_df), ]             # trimming  the outliers
df_trimmed

df.shape,df_trimmed.shape                         # shape of original dataframe and trimmed dataframe
sns.boxplot(df_trimmed.chas)                        # checking outliers in trimmed dataframe

# replacing outliers to their upper limit and lower limit respectively

df['df_replaced'] = pd.DataFrame(np.where(df['chas'] > upper_limit, upper_limit, np.where(df['chas'] < lower_limit, lower_limit, df['chas'])))

plt.boxplot(df.df_replaced)                       # checking outliers in replaced dataframe

# replacing outliers using winsorization

# initialising winsorizer with iqr as capping method fold up to 1.5
winsor = Winsorizer(capping_method='iqr',tail='both',fold=1.5,variables=['chas'])

df_t = winsor.fit_transform(df[['chas']])          # transforming for replacing outliers         
sns.boxplot(df_t.chas)                             # checking for outliers  

# checking outliers for nox feature **********************************************

sns.boxplot(df.nox)                               # no outlier detected


# checking outliers for rm feature ***********************************************

sns.boxplot(df.rm)                                # outliers detected

Q1 = df.rm.quantile(0.25)                        # calculating lower quartile
Q1
Q3 = df.rm.quantile(0.75)                        # calculating upper quartile
Q3
IQR = Q3 - Q1                                      # calculating IQR
IQR
upper_limit = df.rm.quantile(0.75) +1.5*IQR      # calculating upper limit 
upper_limit

lower_limit = df.rm.quantile(0.25) -1.5*IQR      # calculating lower limit
lower_limit
# detecting outliers in terms of true

outliers_df = np.where((df.rm > upper_limit), True, np.where(df.rm< lower_limit, True, False))
outliers_df
df_trimmed = df.loc[~(outliers_df), ]             # trimming  the outliers
df_trimmed

df.shape,df_trimmed.shape                         # shape of original dataframe and trimmed dataframe
sns.boxplot(df_trimmed.rm)                        # checking outliers in trimmed dataframe

# replacing outliers to their upper limit and lower limit respectively

df['df_replaced'] = pd.DataFrame(np.where(df['rm'] > upper_limit, upper_limit, np.where(df['rm'] < lower_limit, lower_limit, df['rm'])))

plt.boxplot(df.df_replaced)                       # checking outliers in replaced dataframe

# replacing outliers using winsorization

# initialising winsorizer with iqr as capping method fold up to 1.5
winsor = Winsorizer(capping_method='iqr',tail='both',fold=1.5,variables=['rm'])

df_t = winsor.fit_transform(df[['rm']])          # transforming for replacing outliers         
sns.boxplot(df_t.rm)                             # checking for outliers  


# checking outliers for age feature **********************************************

sns.boxplot(df.age)                              # no outlier detected


# checking outlier for dis feature ***********************************************

sns.boxplot(df.dis)                              # outliers detected

Q1 = df.dis.quantile(0.25)                        # calculating lower quartile
Q1
Q3 = df.dis.quantile(0.75)                        # calculating upper quartile
Q3
IQR = Q3 - Q1                                      # calculating IQR
IQR
upper_limit = df.dis.quantile(0.75) +1.5*IQR      # calculating upper limit 
upper_limit

lower_limit = df.dis.quantile(0.25) -1.5*IQR      # calculating lower limit
lower_limit
# detecting outliers in terms of true

outliers_df = np.where((df.dis > upper_limit), True, np.where(df.dis< lower_limit, True, False))
outliers_df
df_trimmed = df.loc[~(outliers_df), ]             # trimming  the outliers
df_trimmed

df.shape,df_trimmed.shape                         # shape of original dataframe and trimmed dataframe
sns.boxplot(df_trimmed.dis)                        # checking outliers in trimmed dataframe

# replacing outliers to their upper limit and lower limit respectively

df['df_replaced'] = pd.DataFrame(np.where(df['dis'] > upper_limit, upper_limit, np.where(df['dis'] < lower_limit, lower_limit, df['dis'])))

plt.boxplot(df.df_replaced)                       # checking outliers in replaced dataframe

# replacing outliers using winsorization

# initialising winsorizer with iqr as capping method fold up to 1.5
winsor = Winsorizer(capping_method='iqr',tail='both',fold=1.5,variables=['dis'])

df_t = winsor.fit_transform(df[['dis']])          # transforming for replacing outliers         
sns.boxplot(df_t.dis)                             # checking for outliers  


# checking outliers for rad feature **********************************************

sns.boxplot(df.rad)                               # no outlier detected

# checking outliers for tax feature **********************************************
 
sns.boxplot(df.tax)                               # no outliers detected

# checking outliers for ptratio feature ******************************************

sns.boxplot(df.ptratio)                           # outliers detected

Q1 = df.ptratio.quantile(0.25)                        # calculating lower quartile
Q1
Q3 = df.ptratio.quantile(0.75)                        # calculating upper quartile
Q3
IQR = Q3 - Q1                                      # calculating IQR
IQR
upper_limit = df.ptratio.quantile(0.75) +1.5*IQR      # calculating upper limit 
upper_limit

lower_limit = df.ptratio.quantile(0.25) -1.5*IQR      # calculating lower limit
lower_limit
# detecting outliers in terms of true

outliers_df = np.where((df.ptratio > upper_limit), True, np.where(df.ptratio< lower_limit, True, False))
outliers_df
df_trimmed = df.loc[~(outliers_df), ]             # trimming  the outliers
df_trimmed

df.shape,df_trimmed.shape                         # shape of original dataframe and trimmed dataframe
sns.boxplot(df_trimmed.ptratio)                        # checking outliers in trimmed dataframe

# replacing outliers to their upper limit and lower limit respectively

df['df_replaced'] = pd.DataFrame(np.where(df['ptratio'] > upper_limit, upper_limit, np.where(df['ptratio'] < lower_limit, lower_limit, df['ptratio'])))

plt.boxplot(df.df_replaced)                       # checking outliers in replaced dataframe

# replacing outliers using winsorization

# initialising winsorizer with iqr as capping method fold up to 1.5
winsor = Winsorizer(capping_method='iqr',tail='both',fold=1.5,variables=['ptratio'])

df_t = winsor.fit_transform(df[['ptratio']])          # transforming for replacing outliers         
sns.boxplot(df_t.ptratio)                             # checking for outliers  


# checking outliers for black feature *********************************************

sns.boxplot(df.black)                                 # outliers detected
  
Q1 = df.black.quantile(0.25)                        # calculating lower quartile
Q1
Q3 = df.black.quantile(0.75)                        # calculating upper quartile
Q3
IQR = Q3 - Q1                                      # calculating IQR
IQR
upper_limit = df.black.quantile(0.75) +1.5*IQR      # calculating upper limit 
upper_limit

lower_limit = df.black.quantile(0.25) -1.5*IQR      # calculating lower limit
lower_limit
# detecting outliers in terms of true

outliers_df = np.where((df.black > upper_limit), True, np.where(df.black< lower_limit, True, False))
outliers_df
df_trimmed = df.loc[~(outliers_df), ]             # trimming  the outliers
df_trimmed

df.shape,df_trimmed.shape                         # shape of original dataframe and trimmed dataframe
sns.boxplot(df_trimmed.black)                        # checking outliers in trimmed dataframe

# replacing outliers to their upper limit and lower limit respectively

df['df_replaced'] = pd.DataFrame(np.where(df['black'] > upper_limit, upper_limit, np.where(df['black'] < lower_limit, lower_limit, df['black'])))

plt.boxplot(df.df_replaced)                       # checking outliers in replaced dataframe

# replacing outliers using winsorization

# initialising winsorizer with iqr as capping method fold up to 1.5
winsor = Winsorizer(capping_method='iqr',tail='both',fold=1.5,variables=['black'])

df_t = winsor.fit_transform(df[['black']])          # transforming for replacing outliers         
sns.boxplot(df_t.black)                             # checking for outliers  


# checking outliers for lstat   feature *********************************************

sns.boxplot(df.lstat )                             # outliers detected 

Q1 = df.lstat.quantile(0.25)                        # calculating lower quartile
Q1
Q3 = df.lstat.quantile(0.75)                        # calculating upper quartile
Q3
IQR = Q3 - Q1                                      # calculating IQR
IQR
upper_limit = df.lstat.quantile(0.75) +1.5*IQR      # calculating upper limit 
upper_limit

lower_limit = df.lstat.quantile(0.25) -1.5*IQR      # calculating lower limit
lower_limit
# detecting outliers in terms of true

outliers_df = np.where((df.lstat > upper_limit), True, np.where(df.lstat< lower_limit, True, False))
outliers_df
df_trimmed = df.loc[~(outliers_df), ]             # trimming  the outliers
df_trimmed

df.shape,df_trimmed.shape                         # shape of original dataframe and trimmed dataframe
sns.boxplot(df_trimmed.lstat)                        # checking outliers in trimmed dataframe

# replacing outliers to their upper limit and lower limit respectively

df['df_replaced'] = pd.DataFrame(np.where(df['lstat'] > upper_limit, upper_limit, np.where(df['lstat'] < lower_limit, lower_limit, df['lstat'])))

plt.boxplot(df.df_replaced)                       # checking outliers in replaced dataframe

# replacing outliers using winsorization

# initialising winsorizer with iqr as capping method fold up to 1.5
winsor = Winsorizer(capping_method='iqr',tail='both',fold=1.5,variables=['lstat'])

df_t = winsor.fit_transform(df[['lstat']])          # transforming for replacing outliers         
sns.boxplot(df_t.lstat)                             # checking for outliers  


# checking outliers for medv feature *********************************************

sns.boxplot(df.medv)

Q1 = df.medv.quantile(0.25)                        # calculating lower quartile
Q1
Q3 = df.medv.quantile(0.75)                        # calculating upper quartile
Q3
IQR = Q3 - Q1                                      # calculating IQR
IQR
upper_limit = df.medv.quantile(0.75) +1.5*IQR      # calculating upper limit 
upper_limit

lower_limit = df.medv.quantile(0.25) -1.5*IQR      # calculating lower limit
lower_limit
# detecting outliers in terms of true

outliers_df = np.where((df.medv > upper_limit), True, np.where(df.medv< lower_limit, True, False))
outliers_df
df_trimmed = df.loc[~(outliers_df), ]             # trimming  the outliers
df_trimmed

df.shape,df_trimmed.shape                         # shape of original dataframe and trimmed dataframe
sns.boxplot(df_trimmed.medv)                        # checking outliers in trimmed dataframe

# replacing outliers to their upper limit and lower limit respectively

df['df_replaced'] = pd.DataFrame(np.where(df['medv'] > upper_limit, upper_limit, np.where(df['medv'] < lower_limit, lower_limit, df['medv'])))

plt.boxplot(df.df_replaced)                       # checking outliers in replaced dataframe

# replacing outliers using winsorization

# initialising winsorizer with iqr as capping method fold up to 1.5
winsor = Winsorizer(capping_method='iqr',tail='both',fold=1.5,variables=['medv'])

df_t = winsor.fit_transform(df[['medv']])          # transforming for replacing outliers         
sns.boxplot(df_t.medv)                             # checking for outliers 





















