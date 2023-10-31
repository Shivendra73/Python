#delete


import pymysql
con=pymysql.connect(host="localhost",user="root",password="root",database="mydb15")

cur1=con.cursor()

cur1.execute("delete from emp where eid=105")
con.commit()

cur1.execute("select * from emp")

for row in cur1:
    print(row)
    
cur1.close()
con.close()
