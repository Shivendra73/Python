


#when a record is updated--->means rowcount should be 1.
#if rowcount!= 1 ----->record not updated,means account is not available,so perform rollback
#if rowcount== 1 ----->means 1 row updated,account available,so perform commit.

import pymysql
class AccountNoDoesNotExist(Exception):   #userdefined exception
    pass
con=None
con=pymysql.connect(host='localhost',user='root',password='root',database='mydb15')
cur=con.cursor()
try:
    saccno=input("Enter SOURCE ACCOUNT NO:")
    tamt=input("Enter TRANSFER AMOUNT:")
    query1='update customer set bal=bal-'+tamt+' where accno='+saccno #removing from one account
    #print(query1)
    cur.execute(query1)
    print(cur.rowcount)
    if(cur.rowcount!=1):     #if ==1,means updated,account exists.
         print("Saccno is not available")
         raise AccountNoDoesNotExist  
         #when exception raised,next stmts r not executed,goes to except block and rollback
    daccno=input("Enter DESTINATION ACCOUNT NO:")#if query1 executes only then this will be executed       
    query2='update customer set bal=bal+ '+tamt+' where accno='+daccno #adding in another account
    #print(query2)
    cur.execute(query2) #if query1 and query2 wont execute--->sqlexception,handled by except block
    print(cur.rowcount)
    if(cur.rowcount!=1):
         print("daccno is not available")
         raise AccounNoDoesNotExist
    cur.close()
    con.commit()               
except:
    con.rollback()
    print("TRANSACTION FAILED")
finally:
    if(con!=None):   #if con=None, no need to close
         con.close()

