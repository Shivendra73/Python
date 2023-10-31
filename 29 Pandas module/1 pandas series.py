'''
pip install pandas
main components of pandas are
i)Series
ii)DataFrame.

i)Series is nothing but a column
iiDataFrame is a multi-dimensional table made up of a collection of Series.

ex:
    series   series    DataFrame
      eid    ename     eid ename
      101    Miller    101 Miller
      102 +  Blake  =  102 Blake
      103    James     103 James
      104    John      104 John

'''

#pandas series:

#Series is a one-dimensional labeled array

#A pandas Series can be created using the following constructor −

# pandas.Series( data, index, dtype)
#1)data :data takes various forms like ndarray, list, constants

#2)index :Index values must be unique.

#3)dtype : dtype is for data type.
#----------------------------------------------------------------------------------------------------
#1)Creating a Empty series
import pandas as pd
s = pd.Series()
print(s)
'''
output:
Series([], dtype: float64) '''
print("\n")

#----------------------------------------------------------------------------------------------------
#2)Create a Series from dictionary
import pandas as pd
data={"maths":90,"phy":60,"chem":50}
s = pd.Series(data)   #here maths,phy,chme will be taken as indices
print(s)
'''
Output:
maths    90
phy      60
chem     50 '''

print(s["chem"])  #Accessing the element using index
#output: 50
#----------------------------------------------------------------------------------------------------
#3)Create a Series from a list
import pandas as pd
x=[10,20,30,40,50]
s = pd.Series(x) #default the index starts with 0
print(s)
'''
Output:
0    10
1    20
2    30
3    40
4    50 '''
print(s[3])
#creating our own indexes:
s = pd.Series(x,index=['a','b','c','d','e']) #here indexes are a,b,c,d,e
print(s)
'''
output:
a    10
b    20
c    30
d    40
e    50 '''

print(s["b"])
#output:20
#---------------------------------------------------------------------------------------------------
#4)Accessing a series element
print(s[0]) #Accessing the 1st element
print("\n")
#5)retrieve the first three elements
print(s[:3])
#6)retrieve the last three element
print(s[-3:])

#7)Accessing element using index
print(s['a'])

#8) Accessing multiple elements
print(s[['a','c','d']])
#---------------------------------------------------------------------------------------------------

