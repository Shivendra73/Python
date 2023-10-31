#update:

#update or increment the salary of Blake by 5000

import pymysql
con=pymysql.connect(host="localhost",user="root",password="root",database="mydb15")

cur1=con.cursor()

cur1.execute("update emp set sal=sal+5000 where ename='Blake'")
con.commit()

cur1.execute("select * from emp")

for row in cur1:
    print(row)
    
cur1.close()
con.close()
