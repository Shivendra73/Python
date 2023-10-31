f=open("demo1.txt",mode="r") #whenever we call open fn,it internally creates a file object

for p in f:
    print(p)
f.close()
