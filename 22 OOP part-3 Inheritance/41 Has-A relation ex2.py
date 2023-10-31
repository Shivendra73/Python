

#within the same class accessing the properties
class A:
    x=10
    def __init__(self):
        self.y=20
        print("base class constructor....")
    def m1(self):
        print("from m1.....")

    def m2(self):
        print("from m2.....")
        print(A.x) #Accessing SV
        print(self.y)#Accessing NSV
        self.m1() #Accessing method m1 using self
a1=A()
a1.m2() #when m2 is called by a1,a1 address is stored in self of m2
        #using self of m2,we can access m1() and y

