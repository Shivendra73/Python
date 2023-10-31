#Read 2 .py files and write into a single .py file

f=open("C:/python1130amm/lists/3 List functions.py","r")
x=f.read()
print(x,type(x))
f.close()

f1=open("C:/python1130amm/lists/7 list address.py","r")
y=f1.read()
print(y,type(y))
f1.close()

f2=open("merge.py","w")
for p in x:
    f2.write(p)
for q in y:
    f2.write(q)
f2.close()      #here we need to cloe the file then omly the operation will b perfored

f3=open("merge.py","r")
print(f3.read())
f3.close()
