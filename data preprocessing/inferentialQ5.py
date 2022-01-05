import pandas as pd

df = pd.read_excel("inferential.xlsx")   #importing file
df

df.describe()   # calculating mean,median,sd, quartiles,maxvalue and minvalue

df.var()       #  calculating variance

df.mode()      # calculating  mode

pointsrange = max(df.Points) - min(df.Points) # calculating range of Points
pointsrange

scorerange = max(df.Score) - min(df.Score)   # calculating range of Score
scorerange

weighrange = max(df.Weigh) - min(df.Weigh)   # calculating range of Weigh
weighrange
