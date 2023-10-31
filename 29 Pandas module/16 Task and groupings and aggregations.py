
import pandas as pd
#pd.set_option('display.height',1000)
#pd.set_option('display.max_rows',5000)
#pd.set_option('display.max_columns',500)
#pd.set_option('display.width',1000)
#df.head(100)
#df.tail(100)

# Load data from a csv file (or) Excel file
#A CSV file can be loaded into a pandas using the function---->pandas.read_csv()
#A Excel file also we can read as pandas.read_excel()

df = pd.read_csv('orders.csv') #df is a Dataframe
#print (df)

#Reading Specific Rows of particular column--->5rows
print (df[0:5]['customer'])

#Reading Specific Columns
'''We use the multi-axes indexing method called loc() for this purpose.
We choose to display the customer and order column for all the rows.'''
#print (df.loc[:,['customer','order']])

#Reading Specific Columns and Rows
'''The read_csv function of the pandas library can also be used to read some specific columns and specific rows.
We use the multi-axes indexing method called .loc() for this purpose.
We choose to display the customer and order column for some of the rows.'''
print(df.loc[[1,3,5],['customer','order']])

#Reading Specific Columns for a Range of Rows
print (df.loc[2:6,['customer','order']])


#How many rows the dataset has i.e how many total orders were made--->using count()
#1.No of orders----->using count()
orders=df['order'].count()
print("NO OF ORDERS:",orders)

#2.Total order value(TOV) generated for all orders ---->sum()
tot_rev=df['revenue'].sum()
print("TOTAL ORDER VALUE:",tot_rev)      

#3.Average order value(AOV) generated for all orders ---->mean()
avg_rev=df['revenue'].mean()
print("AVERAGE ORDER VALUE(AOV):",avg_rev)

#4.Max order value  ---->max()
max_rev=df['revenue'].max()
print("MAX ORDER VALUE:",max_rev)

#5.Min order value  ---->min()
min_rev=df['revenue'].min()
print("MIN ORDER VALUE:",min_rev)



# TASK-1. Calculate total number of orders per customer; 
orders_cust=df.groupby('customer')['order'].count()
print("Total No of orders per customer:\n",orders_cust)

#TASK-2: Calculate TOV per customer, TOV  - Total revenue;
TOV_cust=df.groupby('customer')['revenue'].sum()  
print("TOV per Customer:\n",TOV_cust)

#TASK-3: Calculate AOV per customer, AOV  - average revenue;
AOV_cust=df.groupby('customer')['revenue'].mean()
print("AOV per Customer: \n",AOV_cust)

# Calculate the count of orders based on order_state
cnt=df.groupby('order_state')['order_state'].count()
print("order_state:\n",cnt)



#multi grouping
#df.groupby(['col1', 'col2']).agg({'col3': [min, max, sum]})

#-------------------------------------------------------------------------------

#Filtering data:
#Selecting rows in pandas DataFrame based on conditions

#I want those orders whose ordervalue(revenue) >100
df1 = df[df['revenue'] > 100]
print(df1)
print("\n")
#or
df2 = df.loc[df['revenue'] > 100]
print(df2)
print("\n\n\n")

print("\n")

#I want those orders which are not completed 
#ex:2
df3 = df.loc[df['order_state']!='completed']
print(df3)







