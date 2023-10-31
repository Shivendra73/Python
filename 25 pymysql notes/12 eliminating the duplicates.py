#Eliminating the duplicates

import pymysql
con=pymysql.connect(host="localhost",user="root",password="root",database="mydb15")

cur1=con.cursor()

cur1.execute("create table empres3 as select distinct(eid),ename,sal,sex,dno,city from empres")

cur1.execute("select * from empres3")

for p in cur1:
    print(p)
cur1.close()
con.close()
