
#Creating a table from another table

import pymysql
con=pymysql.connect(host="localhost",user="root",password="root",database="mydb15")

cur1=con.cursor()

cur1.execute("create table emp1 like emp")

#Inserting data from one table to another
cur1.execute("insert into emp1 select * from emp")
con.commit()

#Retrieving the data
cur1.execute("select * from emp1")

for p in cur1:
    print(p)
cur1.close()
con.close()
