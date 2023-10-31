


#rowcount : It returns how many rows that are affected by an operation.
#select stmt------>records not modified,so returns 0
#update stmt------>returns number of affected rows
#delete stmt------>returns number of affected rows
#after executing the sql query,no of records,which are affected in database table count
#is stored into the rowcount attribute of cursor object.


import pymysql

con = pymysql.connect(host='localhost',user='root',password='root',database='mydb15')
cur = con.cursor()
cur.execute("update emp set sal=sal+5000 where dno=12") #returns rowcount->2,if i give deptno=50,no rows affected
#cur.execute("select * from emp")  #returns rowcount--->0,as no records affected
con.commit()
print(cur.rowcount)
cur.close()
con.close()
#as in deptno 12,there r only 2 records,so 2 records affected,so 2 is returned


