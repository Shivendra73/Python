#Reading data from a Excel File
import pandas as pd

df = pd.read_excel('C:/data/emp.xlsx')  #Note: read_excel() for reading from excel file
print(df)

print("\n\n")


#Note: xlrd module should be installed before reading this excel file.
