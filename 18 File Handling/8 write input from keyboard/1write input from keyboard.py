

#Accepting i/p from keyboard and writing into a file
f=open("emp.txt",mode="w+")   #if mode="w+", it can write and read

emp1=input("Enter Emp Details:")
f.write(emp1)         #file already exists, so it truncates
f.seek(0)
print(f.read())
f.close()              #if file doesnt exist, it creates a new file

'''
f1=open("sample.txt")
print(f1.read())    
f1.close() 
'''
