import pandas as pd
from openpyxl.workbook import Workbook


df_csv = pd.read_csv("Names.csv", header=None)
df_csv.columns = ["First", "Last", "Address", "City", "State", "Area Code", "AC2"]

#print(df_csv[["Last","State"]])

print(df_csv["First"][0:3])



 