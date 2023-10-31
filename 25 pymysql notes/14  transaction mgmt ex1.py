

#Transaction management->removing from one account and adding in another account
#first create table customer in database and insert values...
#create table customer(accno int,custname varchar(10),bal int);
#insert into customer values(1001,'Rama',90000.00);
#insert into customer values(1002,'Sita',60000.00);
#commit;
import pymysql
con=pymysql.connect(host='localhost',user='root',password='root',database='mydb15')
cur=con.cursor()
saccno=input("Enter SOURCE ACCOUNT NO:")      
daccno=input("Enter DESTINATION ACCOUNT NO:")
tamt=input("Enter TRANSFER AMOUNT:")
query1='update customer set bal = bal -'+tamt+' where accno='+saccno #removing from one account
print(query1)
query2='update customer set bal = bal +'+tamt+' where accno='+daccno #adding in another account
print(query2)

try:
    cur.execute(query1)
    cur.execute(query2)  #if any query gives error ctrl goes to except block (ex: if table doesn't exist)
    cur.close()
    con.commit() #here if bodth queries executes only perform commit(),else rollback()
    
except:
    con.rollback()
    print("Error")
    
con.close()


#here whenever we remove from one account and while adding if the account doesnt exist,then the amount is lost,
# so to overcome,see the next program
