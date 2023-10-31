f=open("hello1.txt")

s1=f.read()
print(s1,type(s1),len(s1))
print(s1.find("pune"))
print(f.tell())
f.seek(f.tell()-5)
print(f.tell())
print(f.read())

