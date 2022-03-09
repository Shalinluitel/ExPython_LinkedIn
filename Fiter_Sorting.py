from tkinter.tix import COLUMN
import pandas as pd

df = pd.read_csv("Names.csv", header=None)
df.columns = ["First",'Last','Address','City','State','Area_Code',"Income"]

#print(df)

#Filter data based on columns
#print(df.loc[df['City'] == "Riverside"])


#Filter data based on 2 properties, here, city to riverside and first name to John
#print(df.loc[(df["City"] == "Riverside") & (df["First"] == "John")])

#Make another table a function of one table or mathematical merge between them
df["Tax%"] = df["Income"].apply(lambda x: 0.15 if 10000 < x < 40000 else 0.2 if 40000 < x < 80000 else 0.25)
df["Tax_Amount"] = df["Income"] * df["Tax%"]
#print(df)

to_drop = ["Area_Code", "First", "Address"]
df.drop(columns = to_drop, inplace = True)
#print(df)

df["Test_Col"] = 0
df.loc[df["Income"] < 60000, "Test_Col"] = 1
#print(df)
print(df.groupby(["Test_Col"]).mean().sort_values("Income"))










