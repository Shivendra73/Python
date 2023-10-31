
#Reading data from one file and writing data to other file
#I-method
'''
f=open("demo1.txt","r")
x=f.readlines()
f.close() 

f1=open("demo2.txt","w")
for p in x:
    f1.write(p)
f1.close()      #here we need to close the file then omly the operation will b perfored

f2=open("demo2.txt","r")
print(f2.read())
f2.close() '''

#II-method

#using read()
f=open("demo1.txt","r")
x=f.read()
print(x,type(x))
f.close() 

f1=open("demo2.txt","w")
for p in x:
    f1.write(p)
f1.close()      #here we need to cloe the file then omly the operation will b perfored

f2=open("demo2.txt","r")
print(f2.read())
f2.close() 




