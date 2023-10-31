
#Creating emp table
#Creating multiple cursor objects
#cur1---->for creating table
#cur2---->for inserting data
#cur3---->for retrieving data

import pymysql

#Creating connection object

con=pymysql.connect(host="localhost",user="root",password="root",database="mydb15")

#Creating cursor object
cur1=con.cursor() #on connection object(con),if we pass cursor()method then cursor object(cur1)
                  #is created.

#Creating cur1 object for creating table
cur1.execute("create table emp(eid int,ename varchar(20),sal int,sex varchar(1),dno int,
             city varchar(10))")
print("TABLE CREATED SUCESSFULLY!!!!")

#Creating cur2 object for inserting data
cur2=con.cursor()
cur2.execute("insert into emp values(101,'Miller',10000,'m',11,'pune'),(102,'Blake',20000,'m',
             12,'hyd'),(103,'Sony',30000,'f',11,'pune'),(104,'Sita',40000,'f',12,'hyd'),
            (105,'James',50000,'m',13,'hyd')")
print("DATA INSERTED SUCCESSFULLY!!!")
con.commit()
#Creating cur3 object for Retrieving data
cur3=con.cursor()
cur3.execute("select * from emp") #The o/p of sql query is stored within the cur3 object

#Apply for loop and get one by one record from cur3 object

for row in cur3:
    print(row)

cur1.close()
cur2.close()
cur3.close()

con.close()

#Note: we can perform all the above operations using single cursor object
#      but for retrieving data from multiple tables then use multiple cursor objects

#o/p:

mysql> select * from emp;
+------+--------+-------+------+------+------+
| eid  | ename  | sal   | sex  | dno  | city |
+------+--------+-------+------+------+------+
|  101 | Miller | 10000 | m    |   11 | pune |
|  102 | Blake  | 20000 | m    |   12 | hyd  |
|  103 | Sony   | 30000 | f    |   11 | pune |
|  104 | Sita   | 40000 | f    |   12 | hyd  |
|  105 | James  | 50000 | m    |   13 | hyd  |
+------+--------+-------+------+------+------+







