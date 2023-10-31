#append mode
f=open("sample.txt",mode="a+")
x=input("Enter new Emp Details:")
f.write("\n")
f.write(x) 
f.seek(0)
print(f.read())    
f.close()
