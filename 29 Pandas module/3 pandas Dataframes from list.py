#Pandas DataFrame:
#A pandas DataFrame can be created using the following class constructor −

#pandas.DataFrame( data, index, columns, dtype)
'''
1)data: data takes various forms like ndarray, series, lists, dict, constants ,files and also another DataFrame.

2)index:For the row labels,

3)columns :For column labels4	

4)dtype: Data type of each column.


A pandas DataFrame can be created using various inputs like −
1)Lists
2)dict
3)Series
4)Numpy ndarrays
5)Another DataFrame
6)Files  (CSV,EXCEL,json)
'''
#-----------------------------------------------------------------------------------------------------
#1)Creating a empty Dataframe
import pandas as pd
df = pd.DataFrame()
print(df)
print("\n")
#-----------------------------------------------------------------------------------------------------
#2) Create a DataFrame from Lists

import pandas as pd
cities = ["Pune","mumbai","chennai","hyd"]
df = pd.DataFrame(cities)
print(df)
print("\n")
'''
o/p:
         0
0     Pune
1   mumbai
2  chennai
3      hyd '''
#-----------------------------------------------------------------------------------------------------
#3)Creating a Dataframe from nestedlists
import pandas as pd
data = [['Miller',10000],['Blake',20000],['James',30000]]
df = pd.DataFrame(data,columns=['NAME','SAL'])
print(df)
print("\n")

#o/p:
'''
     NAME    SAL
0  Miller  10000
1   Blake  20000
2   James  30000 '''
    
#-----------------------------------------------------------------------------------------------------
#4) Creating a DataFrame from a list of Dictionaries

import pandas as pd
data = [{'LG': 10, 'SONY': 20},{'LG': 5, 'SONY': 10, 'SAMSUNG': 20}]
df = pd.DataFrame(data)
print(df)

'''
o/p:
   LG  SONY  SAMSUNG
0  10    20      NaN
1   5    10     20.0 '''
print(df.iloc[0])
#-----------------------------------------------------------------------------------------------------

#5) Creating our own indexes(string indexes)

import pandas as pd
data = [{'LG': 10, 'SONY': 20},{'LG': 5, 'SONY': 10, 'SAMSUNG': 20}]
df = pd.DataFrame(data,index=["first","second"])
print(df)
'''
o/p:
        LG  SONY  SAMSUNG
first   10    20      NaN
second   5    10     20.0 '''



#-----------------------------------------------------------------------------------------------------














