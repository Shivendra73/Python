#openining and Reading multiple files

f1=open('demo1.txt',mode='r')
print(f1.read())
f1.close()

print("\n")

f2=open('C:/python630am/string3.py',mode='r')
print(f2.read())

print("\n")

f3=open('C:/python1/sample.java',mode='r')
print(f3.read())

print("\n")

f4=open('F:/emp1.csv',mode='r')
print(f4.read())


print("\n")

for p in f4:
    print(p)


