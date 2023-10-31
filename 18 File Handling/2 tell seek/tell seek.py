

#tell() : tells where currently the cursor is
#seek() :moving the cursor to the desired position.

f=open("sample.txt")
print(f.tell())  #tells the current cursor position
print(f.read())
print(f.tell())
f.seek(8)      #moving the cursor to desired position
print(f.tell())
print(f.read())
print(f.tell())
f.seek(11)
print(f.read(4)) #reads 4 characters from current position
print(f.tell())
f.close() 


