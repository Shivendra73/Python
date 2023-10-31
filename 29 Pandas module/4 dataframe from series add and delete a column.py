
#Creating Pandas Dataframes from series

#Create a DataFrame from Dict of Series
#Dictionary of Series can be passed to a DataFrame.
#The resultant index is the union of all the series indexes passed.

import pandas as pd

d = {'student1' : pd.Series([90, 80, 70], index=['maths', 'phy', 'chem']),
   'student2' : pd.Series([50,70,60], index=['maths', 'phy', 'chem'])}
print(d,type(d),len(d))


df = pd.DataFrame(d)
print(df)
#o/p:
'''
       student1  student2
maths        90        50
phy          80        70
chem         70        60
'''
print("\n")
#-------------------------------------------------------------------------------------------------
#2)Column selection
print(df["student1"])

#o/p:
'''
maths    90
phy      80
chem     70
'''
print(df.loc['maths'])
#o/p:
#student1    90
#student2    50
#-------------------------------------------------------------------------------------------------
#3)Column Adding: 

# Adding a new column to an existing DataFrame with column label by passing new series

print ("Adding a new column by passing as Series:")
df['student3']=pd.Series([75,80,65],index=['maths', 'phy', 'chem'])
print(df)

print ("Adding a new columns using the existing columns in DataFrame:")
df['Total']=df['student1']+df['student2']+df['student3']
df['Average']=(df['student1']+df['student2']+df['student3'])/3
print(df)

#----------------------------------------------------------------------------------------------------
#4) Deleting a column: 2ways
#1.using del keyword
print ("Deleting the first column using del:")
del df['student1']
print(df)
print("\n")

#2.using pop function
print ("Deleting another column using POP function:")
df.pop('student2')
print(df)

#-------------------------------------------------------------------------------------------------
#5)Addition of Rows using append()
#This function will append the rows at the end.

import pandas as pd

df1 = pd.DataFrame([["Ajay",20000], ["James", 50000]], columns = ['NAME','SALARY'])
df2 = pd.DataFrame([["Naresh",60000], ["Blake",80000]], columns = ['NAME','SALARY'])

df = df1.append(df2)
print(df)
print("\n")
'''
o/p:
     NAME  SALARY
0    Ajay   20000
1   James   50000
0  Naresh   60000
1   Blake   80000
'''

#--------------------------------------------------------------------------------------------------
#Deletion of Rows using drop()
#Use index label to delete or drop rows from a DataFrame.
#If label is duplicated, then multiple rows will be dropped.

df = df.drop(0)
print(df)

'''
o/p:
    NAME  SALARY
1  James   50000
1  Blake   80000
'''

#-------------------------------------------------------------------------------------------------

