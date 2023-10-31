

#Reading data from a database using Pandas
import pandas as pd
import pymysql
con=pymysql.connect(host='localhost',user='root',password='root',database='mydb8')  #con--->connection object

df = pd.read_sql_query("SELECT * FROM customer", con)
print(df)




