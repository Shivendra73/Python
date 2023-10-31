
#Filtering data from a Dataframe

# importing pandas 
import pandas as pd 
  
data = {  
 'Name': ['Miller','Blake','James','Jimmy','Sony','Ruby' ], 
 'Age': [23,24,22,25,23,22],
 'Gender':['m','m','m','f','f','f'],
 'Branch': ['CSE','ECE','EEE','IT','CSE','ECE'], 
 'Percentage': [84,82,78,76,68,56],
 } 
  
# create a dataframe 
df = pd.DataFrame(data,columns = ['Name', 'Age','Gender','Branch', 'Percentage'])  
print(df)  
print("\n")

#-------------------------------------------------------------------------------------------------------
#i.filtering data based on percentage

df1 = df[df['Percentage'] > 80]
print(df1)
#Note: If we filter a Dataframe then the result is also a Dataframe
print("\n")

#or

df1 = df.loc[df['Percentage'] > 80]
print(df1)

print("\n")
#------------------------------------------------------------------------------------------------------

#ii. I want only CSE students

df1 = df[df['Branch'] == 'CSE']
print(df1)

print("\n")
#------------------------------------------------------------------------------------------------------
#iii. I want other than CSE students
df1 = df[df['Branch'] != 'CSE']
print(df1)

print("\n")

#Note : we can use == , != , >= ,<= ,> , < for filtering the data

#-----------------------------------------------------------------------------------------------------
#iv : isin() method()

#ex:
#I require only those students who belong to CSE or IT background

options=['CSE','IT']

df3 = df[df['Branch'].isin(options)]
print(df3)

print("\n")

#or
df4 = df.loc[df['Branch'].isin(options)]
print(df4)

print("\n")
#------------------------------------------------------------------------------------------------------

#V :I want to know those students who are from non-CSE background
options=['CSE','IT']

df5 = df[~df['Branch'].isin(options)]
print(df5)
print("\n")
#------------------------------------------------------------------------------------------------------

#Vi. Providing multiple conditions
#I want those students whose percentage < 70 and are non-CSE Background
df6 = df[(df['Percentage'] < 70) & 
        ~df['Branch'].isin(options)]
print(df6)










 
