#Creating a new database(mydb15) within mysql

import pymysql

#creating connection object
con=pymysql.connect(host="localhost",user="root",password="root")  #con---->connection object

#creating cursor object

cur1=con.cursor() #cur1 is the cursor object.

cur1.execute("create database mydb15")

print("DATABASE CREATED SUCCESSFULLY!!!!")

cur1.close()

con.close()
