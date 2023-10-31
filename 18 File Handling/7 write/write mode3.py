
#writing into a python file
f=open("Test2.py",mode="w")

#entire python file data taken as string and write this string into the file
data='''
x=[10,20,30,40,50]
print(x)
print('sum of list elements=',sum(x))'''

f.write(data)

                       #if file already exists, so it truncates

f.close()              #if file doesnt exist, it creates a new file and writes

f1=open("Test2.py")
print(f1.read())    
f1.close()
