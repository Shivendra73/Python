
#readlines()

f=open("hello.txt","r")
x=f.readlines() # reads all the lines and stores in a list x with \n behaviour
print(x,type(x))        # printing the list x

#printing each line seperately

for p in x:
    print(p)
    
f.close() # whenever we close a file, it will be used by
          #another person


print(x[1])




