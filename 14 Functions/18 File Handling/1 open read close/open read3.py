#Reading multiple files at a time
f1=open("demo1.txt",mode="r")            #reading a .txt file

f2=open("C:/data/sample.java","r")       #reading a java file
f3=open("C:/python1030am/str1.py")       #reading a python file
f4=open("C:/data/emp1.csv","r")
'''
print(f1.read())                         
print(f2.read())
print(f3.read())
print(f4.read())'''

x=[f1,f2,f3,f4]

for p in x:
    for q in p:
        print(q)
    print("\n")




