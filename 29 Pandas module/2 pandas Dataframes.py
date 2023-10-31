
#-----------------------------------------------------------------------------------------------------
#Creating DataFrames

#i) Creating Dataframes from a Dictionary

import pandas as pd
data={
      "enames":["Miller","Blake","James","John"],
      "sals":[10000,20000,30000,40000]
      }

#passing this dictionary(data) to pandas DataFrame Constructor , so that a dataframe gets created

df1=pd.DataFrame(data)   #here df1 is a dataframe
print(df1)
print("\n\n")
'''
o/p:
  enames   sals
0  Miller  10000
1   Blake  20000
2   James  30000
3    John  40000 '''
#Note here by default we get index starting with 0, even we can have our own index
 
#----------------------------------------------------------------------------------------------------
#ex:2 Even we can have index as string type

import pandas as pd
data={
      "Sony":[250,350,200,150,300],
      "LG":[300,180,260,200,150],
      "Lenovo":[300,180,260,200,150]
      }
df2 = pd.DataFrame(data, index=["April","May","June","July","August"])
print(df2)
'''
o/p:
        Sony   LG  Lenovo
April    250  300     300
May      350  180     180
June     200  260     260
July     150  200     200
August   300  150     150 '''
print("\n\n")

#ex:3

#Retrieving particular month data
print(df2.loc["April"])
'''
o/p:
Sony      250
LG        300
Lenovo    300
Name: April, dtype: int64 '''
print("\n\n")

#-----------------------------------------------------------------------------
#4) Indexing and slicing

#a)printing a specific column(series)

print(df2["LG"])
'''
o/p:
April     300
May       180
June      260
July      200
August    150
Name: LG, dtype: int64
'''
#here we see no colname

#b)Printing a Dataframe
print(df2[["LG"]])
'''
o/p:
         LG
April   300
May     180
June    260
July    200
August  150 '''

#c)printing multiple columns as Dataframe)

print(df2[["LG","Sony"]])

'''
o/p:
         LG  Sony
April   300   250
May     180   350
June    260   200
July    200   150
August  150   300
'''

#d)Slicing a Dataframe
#  Retrieving specific rows

x=df2[0:3]
print(x)
'''
o/p:
      Sony   LG  Lenovo
April   250  300     300
May     350  180     180
June    200  260     260
'''
#The result(x) is also a dataframe

#e)More data selection operations
#Using loc and iloc, you can select certain rows in a data set.
#loc uses string indices
#iloc uses integers.

x=df2.loc[["April","May"]]
print(x)

'''
O/p:
       Sony   LG  Lenovo
April   250  300     300
May     350  180     180
'''
#f) iloc
x=df2.iloc[3]
print(x)
'''
o/p:
Sony      150
LG        200
Lenovo    200
Name: July, dtype: int64
'''
#g)getting morethan one column
x=df2.iloc[:,1:3]
print(x)

'''
o/p:
        LG  Lenovo
April   300     300
May     180     180
June    260     260
July    200     200
August  150     150
'''
x=df2.iloc[0:3,1:3]
print(x)

'''
o/p:
       LG  Lenovo
April  300     300
May    180     180
June   260     260
'''
#------------------------------------------------------------------------------
#h) sorting data
#   df.sort_values()
#By default sorts in ascending order
x=df2.sort_values('LG')
print(x)
'''
o/p:
        Sony   LG  Lenovo
August   300  150     150
May      350  180     180
July     150  200     200
June     200  260     260
April    250  300     300
'''
x=df2.sort_values('LG',ascending=False)
print(x)
'''
o/p:

       Sony   LG  Lenovo
April    250  300     300
June     200  260     260
July     150  200     200
May      350  180     180
August   300  150     150

'''
#i) Renaming a dataframe column
#   Renaming Sony to Samsung
x=df2.columns=['Samsung','LG','Lenovo']
print(x)
'''
o/p:

['Samsung', 'LG', 'Lenovo']
'''
#j) Dropping a column
x=df2.drop('LG',axis=1)
print(x)
'''
o/p:
       Samsung  Lenovo
April       250     300
May         350     180
June        200     260
July        150     200
August      300     150
'''
#Dropping a row
x=df2.drop('May')
print(x)

'''
o/p:
      Samsung   LG  Lenovo
April       250  300     300
June        200  260     260
July        150  200     200
August      300  150     150
'''
#k)Adding new columns

df2["oppo"]=df2.eval('LG+100')
print(df2)

'''
o/p:
         Samsung   LG  Lenovo  oppo
April       250  300     300   400
May         350  180     180   280
June        200  260     260   360
July        150  200     200   300
August      300  150     150   250
'''
#Adding a new column---->RedMi
df2["RedMi"]=pd.Series([350,170,250,200,370],index=["April","May","June","July","August"])
print(df2)
#Output:
'''
       Samsung   LG  Lenovo  oppo  RedMi
April       250  300     300   400    350
May         350  180     180   280    170
June        200  260     260   360    250
July        150  200     200   300    200
August      300  150     150   250    370 '''


#Converting a df to excel
df2.to_excel("mobiles.xlsx")


#l)max()
x=df2.LG.max()
print(x)

'''
o/p:300
'''

#m) groupby
x=df2.groupby("Samsung").sum()
print(x)

#n)  Missing values in pandas
#isnull(): will tell  if a column misses a value

print(df2.isnull())

'''
o/p:
       Samsung     LG  Lenovo   oppo
April     False  False   False  False
May       False  False   False  False
June      False  False   False  False
July      False  False   False  False '''

#0)Ranking:
#rank():to rank every column according to its value

print(df2.rank())

'''
o/p:
        Samsung   LG  Lenovo  oppo
April       3.0  5.0     5.0   5.0
May         5.0  2.0     2.0   2.0
June        2.0  4.0     4.0   4.0
July        1.0  3.0     3.0   3.0
August      4.0  1.0     1.0   1.0
'''
#p) Concatenating 2 dataframes
#concat():we can concatenate two or more DataFrames
x=pd.concat([df2,df2])
print(x)

'''o/p:
         Samsung   LG  Lenovo  oppo
April       250  300     300   400
May         350  180     180   280
June        200  260     260   360
July        150  200     200   300
August      300  150     150   250
April       250  300     300   400
May         350  180     180   280
June        200  260     260   360
July        150  200     200   300
August      300  150     150   250 '''

#Note: we can even concat 3 or more dataframes
