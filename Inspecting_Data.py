from operator import index
import pandas as pd
from openpyxl.workbook import Workbook


#Load data and save desired varibles as excel.

df_csv = pd.read_csv("Names.csv", header=None)
df_csv.columns = ["First", "Last", "Address", "City", "State", "Area Code", "AC2"]

#print(df_csv[["Last","State"]])

#print(df_csv["First"][0:3])

#print(df_csv.iloc[3,5])

wanted_values = df_csv[["First", "Last", "State"]]
#print(wanted_values)
stored = wanted_values.to_excel("State_Location.xlsx", index = None)






 