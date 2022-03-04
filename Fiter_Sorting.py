import pandas as pd

df = pd.read_csv("Names.csv", header=None)
df.columns = ["First",'Last','Address','City','State','Area_Code',"Income"]

#print(df)

#Filter data based on columns
#print(df.loc[df['City'] == "Riverside"])

print(df.loc[(df["City"] == "Riverside") & (df["First"] == "John")])