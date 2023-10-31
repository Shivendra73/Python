#merging the tables


import pymysql
con=pymysql.connect(host="localhost",user="root",password="root",database="mydb15")

cur1=con.cursor()

cur1.execute("create table empres as select * from emp1 union all select * from emp2")

cur1.execute("select * from empres")

for p in cur1:
    print(p)
cur1.close()
con.close()
