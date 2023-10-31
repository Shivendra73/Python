
class x:
    def __init__(self):
        print("super class constructor....")
    def m1(self):
        print("from m1.....")
class y(x):
    def __init__(self):
        print("sub class constructor....")
    def m2(self):
        print("from m2....")
y1=y()
print(y1)
y1.m1()
y1.m2()
print(x.__name__) #displays the classname
print(x.__bases__)#to know base class of x
print(y.__bases__)#to know base class of y

#If we have constructor in super class and sub class and if we create
#object of sub class,then sub class constructor only is executed,
#but in java both super class and sub class constuctors are executed.
#to execute super class constuctor also,create object of super class.
x1=x()
