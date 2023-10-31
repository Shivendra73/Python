
#Adding local and Global variables

a=10       #Global variables
b=20

def compute():
    x=30      #Local variables
    y=40
    z=a+b+x+y  #adding all local and global variables
    print("sum=",z)
compute()
