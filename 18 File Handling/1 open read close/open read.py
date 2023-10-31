#opening a file and reading
f=open("demo1.txt",mode="r") #whenever we call open fn,it internally creates a file object
print(f.read())
f.close()
#if we use f.close(),then  object which is created is going to be deleted.
#print(f.read())

