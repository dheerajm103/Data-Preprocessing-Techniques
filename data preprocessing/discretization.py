import pandas as  pd                       # importing library
df = pd.read_csv("iris.csv")               # importing dataset
df

df.drop(['id'], axis=1, inplace=True)     # dropping id column from dataset
df

# converting continious data to discrete classes

sl = pd.cut( df.SepalLength, bins = 4, labels = (0,1,2,3), right = True)   # creating discrete classes for sepal length
sl
sw = pd.cut( df.SepalWidth, bins = 4, labels = (0,1,2,3), right = True)    # creating discrete classes for sepal width
sw
pl = pd.cut( df.PetalLength, bins = 4, labels = (0,1,2,3), right = True)   # creating discrete classes for petal length
pl
pw = pd.cut( df.PetalWidth, bins = 4, labels = (0,1,2,3), right = True)    # creating discrete classes for petal width
pw

# creating dummy variable for species

species = pd.get_dummies(df.Species)             # getting dummy variables for species
species

# creating separate column for dummy column species

species_setosa = species.setosa
species_versicolor = species.versicolor
species_virginica = species.virginica

# creating new dataframe for discrete classes and separate column for dummy columns

newdataframe = pd.DataFrame(columns=["sepallength","sepalwidth","petallength","petalwidth","species.setosa","species.versicolor","species.virginica"])
newdataframe
newdataframe["sepallength"] = sl
newdataframe["sepalwidth"] = sw
newdataframe["petallength"] = pl
newdataframe["petalwidth"] = pw
newdataframe["species.setosa"] = species_setosa
newdataframe["species.versicolor"] = species_versicolor
newdataframe["species.virginica"] = species_virginica
newdataframe
