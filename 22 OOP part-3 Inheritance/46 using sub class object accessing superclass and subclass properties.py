

#super class properties and sub class properties both we can access
#through subclass reference variable

class A:
    a=10
    def m1(self):
        self.b=20
        print("from m1.....")
class B(A):
    c=30
    def m2(self):
        self.d=40
        print("from m2.....")
b1=B()
b1.m1()
b1.m2()

print(B.a)
print(B.c)
print(b1.b)
print(b1.d)


#what is happening internally:
#when we create object(b1) of class B,first it checks whether class B is
#extending any class or not, if it extends then first it creates object of
#class A,then it creates object of class B.

#both the objects (of class A and class B) are stored in same memory location
#and this memory location is taken by python interpreter and returns in-direct address
#and this in-direct address is stored by derived class ref.variable(b1).


                 








        
    
