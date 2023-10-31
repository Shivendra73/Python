#readline()

f=open("hello.txt")

print(f.tell())
print(f.readline()) #reads a particular line and ctrl goes to next line
print(f.tell())
print(f.readline())
print(f.tell())
f.seek(5)
print(f.readline())
print(f.read(5))
print(f.tell())
print(f.readline())
f.seek(17)
print(f.readline())
print(f.tell())
f.seek(31)
print(f.tell(),f.read())
print(f.tell())

f.seek(0)
#applying for loop on the file object(f) and reading each line.
for p in f:
    print(p)


f.close()


