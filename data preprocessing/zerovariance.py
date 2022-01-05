import pandas as  pd                     # importing library
df = pd.read_csv("Z_dataset.csv")        # importing dataset
df

# calculating variance for dataset

df.var()                                 # none feature has variance close to zero
