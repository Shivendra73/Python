#Table to Table copy(CTAS)


import pymysql
con=pymysql.connect(host="localhost",user="root",password="root",database="mydb15")

cur1=con.cursor()

cur1.execute("create table emp2 as select * from emp")

#Retrieving the data
cur1.execute("select * from emp2")

for p in cur1:
    print(p)
    
cur1.close()
con.close()
