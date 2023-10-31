#mysql.connector :for python to connect with mysql

#C:\Python39\Scripts>pip install mysql-connector-python

import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",password="root",database="mydb15")  #con is the connection object
#Always take keyword arguments
cur1=con.cursor()

cur1.execute("update emp set sal=sal+6000 where eid=103")

con.commit()

cur1.execute("select * from emp")

for row in cur1:
    print(row)
print("\n")
