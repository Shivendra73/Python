
#program illustrating inheritance
#program with global,local,static and non-static variables
#Program with function and a method

p=70  #global variable

def show1():       #function ,this function can be accessed by all the classes and methods
    print("hello")
    
class A:
    x=10
    print(x)
    def __init__(self):
        self.y=20
        print("constructor of A")
    def display(self):
        print("Hello....from class A")
        print("p=",p)     #global variable
        show1()

class B(A):  #class B extending class A
    z=30
    print(z)
    def display2(self):
        print("Hello....from class B")
    def show(self):
        global p
        print("x=",B.x)#Accessing  x of class A,SV accessed using class name
        print("y=",self.y)#Accessing y of class A,NSV accessed using self
        print("z=",B.z)
        p=75
        sum1=B.x+self.y+B.z  #sum is a local variable
        print("sum=",sum1)
        print("p=",p)
        self.display()#Accessing method of class A using self
        self.display2()#Accessing method of class B using self
        show1()
b1=B()
b1.show() #b1 address is stored in self of show(),here using self we can also
          #access super class properties such as y and display(),bcoz they are
        #part of class B

#printing all the variables from outside the class
print(B.x)
print(b1.y)
#print(sum1)   #local variables cant be accessed from outside the method

print(p)

        
