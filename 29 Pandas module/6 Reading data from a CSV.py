

#Reading data from a CSV File
import pandas as pd 

df = pd.read_csv('C:/data/emp1.csv')  #Note: read_excel() for reading from excel file
print(df)
print("\n\n")


#To remove the index
df = pd.read_csv('C:/data/emp1.csv',index_col=0)
print(df)

print("\n\n")


