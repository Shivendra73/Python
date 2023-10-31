

#writing into a python file
f=open("Test.py",mode="w")

f.write("x=[10,20,30,40,50]\n")
f.write("print(x)\n")
f.write("print('sum of list elements=',sum(x))")

                       #if file already exists, so it truncates(removes)

f.close()              #if file doesnt exist, it creates a new file and writes

f1=open("Test.py")
print(f1.read())    
f1.close()
