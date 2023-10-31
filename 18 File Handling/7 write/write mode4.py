#writing into a python file to add 2 no's
f=open("C:\python1030amm\Test3.py",mode="w")
f.write("x=30\ny=40\nprint(x+y)") #file already exists, so it truncates
#f.write("y=20 \n")
#f.write("print(x+y) \n")
f.close()              #if file doesnt exist, it creates a new file and writes

f1=open("C:\python1030amm\Test3.py")
print(f1.read())    
f1.close()


#import Test2
