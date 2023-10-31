#creating a table,inserting,retrieving

import pymysql

#Creating connection object
con=pymysql.connect(host="localhost",user="root",password="root",database="mydb15")

#Creating cursor object
cur1=con.cursor()

#Creating table
cur1.execute("create table  student(name varchar(10),rollno int,marks int)")
print("TABLE CREATED SUCCESFULLY")

#inserting data into the table
cur1.execute("insert into student values('Miller',501,94),('Blake',502,98)")
con.commit() #for permanently saving
print("DATA INSERTED SUCCESSFULLY!!!")

#Retrieving data from the table
cur1.execute("select * from student") #the o/p is stored in cur1 object

#Now applying forloop on cur1 object and retrieving onen by one record
for row in cur1:
    print(row)
cur1.close()
con.close()

#ouput: Goto database and check
mysql> show tables;
+------------------+
| Tables_in_mydb15 |
+------------------+
| student          |
+------------------+
1 row in set (0.01 sec)

mysql> select * from student;
+--------+--------+-------+
| name   | rollno | marks |
+--------+--------+-------+
| Miller |    501 |    94 |
| Blake  |    502 |    98 |
+--------+--------+-------+
