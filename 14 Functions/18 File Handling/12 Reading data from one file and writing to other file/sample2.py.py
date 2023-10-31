

f1=open("C:/python1130amm/str2.py","r")
x=f1.readlines()
f1.close()

#f2=open("demo3.py","w+")
f2=open("C:/python1130amm/demo.py","w+")
for line in x:
    f2.write(line)
f2.seek(0)
print(f2.read())
f2.close()

'''
f3=open("demo2.py","r")
print(f3.read())
f3.close()
'''

