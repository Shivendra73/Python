
#By default,we get the records in tuple() format, but i want in list format

import pymysql
con=pymysql.connect(host="localhost",user="root",password="root",database="mydb15")

cur1=con.cursor()

cur1.execute("select * from emp")

for row in cur1:
    print(list(row))
    
print("\n\n")
#------------------------------------------------------------------------------------------
#Store all the records within a list

x=[]

cur1.execute("select * from emp")

for row in cur1:
    x.append(list(row))
print(x,len(x))
print("\n")
#Now modifying within the list
x[2][2]=35000
print(x)

cur1.close()

con.close()



