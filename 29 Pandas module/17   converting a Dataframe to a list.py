
#converting a Dataframe to a list
#df.values.tolist()
from pandas import DataFrame


products = {'Product': ['Tablet','iPhone','Laptop','Monitor'],
            'Price': [9000,18000,45000,10000]
            }

df = DataFrame(products, columns= ['Product', 'Price'])
print(df)
x = df.values.tolist()
print(x,type(x))
print("\n\n")
#------------------------------------------------------------------------------
#ex:2
#If you want to add the column names into your list
#[df.columns.values.tolist()]
from pandas import DataFrame

products = {'Product': ['Tablet','iPhone','Laptop','Monitor'],
            'Price': [250,800,1200,300]
            }

df = DataFrame(products, columns= ['Product', 'Price'])
#printing the column names of DF within a list
print([df.columns.values.tolist()])
#adding column names list  to  other list
p_list = [df.columns.values.tolist()] + df.values.tolist()
print (p_list)

print("\n\n")
#-------------------------------------------------------------------------------
#ex:3

#converting a particular column of a Dataframe to a list
#df['column name'].values.tolist()


from pandas import DataFrame

products = {'Product': ['Tablet','iPhone','Laptop','Monitor'],
            'Price': [250,800,1200,300]
            }

df = DataFrame(products, columns= ['Product', 'Price'])

prod = df['Product'].values.tolist()
print (prod)
print("\n\n")
#----------------------------------------------------------------------------------------------------
#ex:4 appending an additional element into the list
#prod.append('Printer')

from pandas import DataFrame

products = {'Product': ['Tablet','iPhone','Laptop','Monitor'],
            'Price': [250,800,1200,300]
            }

df = DataFrame(products, columns= ['Product', 'Price'])

prod = df['Product'].values.tolist()
prod.append('Printer')

print (prod)

#----------------------------------------------------------------------------------------------------




