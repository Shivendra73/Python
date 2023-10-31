#tell(),read(),seek()

f=open("hello.txt")
print(f.tell())
print(f.read())
print(f.tell())
f.seek(f.tell()-7)
print(f.tell())
print(f.read())
print(f.tell())
f.close()




