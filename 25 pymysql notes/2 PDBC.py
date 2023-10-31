
Python Database connection(PDBC):
--------------------------------

Python to connect with any database,we require a module.

Python to connect with mysql------>pymysql (or) mysql.connector

Python to connect with Oracle----->cx_Oracle

Python to connect with sqlsever--->pyodbc

#External Modules:

Modules which are not part of python software, we call those modules as External modules

These Externalmodules, we need to download and install by using a component called pip.

Pip: Pip is a Application or a Package manager which quickly installs any external
      module which is not part of python software.

Pip is available within the installed folder of Python--->C:\python310\scripts

C:\Users\DELL>cd\

C:\>cd python310\scripts

C:\Python310\Scripts>pip install pymysql


#---------------------------------------------------------------------------------------------
Python to connect with any database and to perform any sql operation , we require 2 objects
1.Connection object

2.cursor object

1)Connection object: If we call connect() function by providing connection the connection
                     parameters then connection object is created

  The folloing connection parameters need to be provided
  1)Host---->localhost or remotehost
  2)Username
  3)password
  4)Databasename

ex: con=pymysql.connect(host="localhost",user="root",password="root",database="mydb14")
    here con is the connection object,we can provide any name for connection object

2)cursor object:
 on connection object,if we pass cursor() method then cursor object is created

 cur1=con.cursor()
 here cur1 is the cursor object

 within this cursor object,we have execute() method,within the execute method, we can specify
 any valid sql query

 cur1.execute("select * from emp")
 The o/p records of the sql query will be stored in the cursor object(cur1)

 










 


  
    













