
#Exception handling,when DB error occurs
#i.e if i give wrong sql query, exception is raised----->sqlexception(or)dberror
#when exception occurs,it wont execute other stmts and terminates abnormally,
#but connection is not closed,
#if connection is not closed,other people cannot access the database
#if 100 people's connection is not closed,then others cannot access the database

import pymysql
con=None  #if connection is not established,in con variable,None is stored
try:    #if connection is established,connection object is stored in con variable
    con=pymysql.connect(host='localhost',user='root',password='root',database='mydb15')
    print("connection established") #if any mistake in connection,
    cursor=con.cursor()   #then except block is executed and prints DB error
    cursor.execute("select * from emp")
    for row in cursor:
        print(row)
    cursor.close()#the stmts within try block are resource allocation stmts
except:
    print("DB error occured")
finally:
    if con!=None:  #These 3 stmts are resource deallocation stmts (or)
        con.close() #resource release stmts
        print("connection closed")




        
        
