
#sub class method calling super class method

class A:
    def m1(self):
        self.x=10
        print("x=",self.x)
        
class B(A):
    def m1(self):
        super().m1()
        self.y=20
        print("y=",self.y)

b1=B()
b1.m1()


#for overriding and executing only userdefined logic,no need of super,
#but to execute pre-defined logic and userdefined-logic,we need super

#for executing only Base class logic(predefined logic)----->No overiding (or) No super() stmt required.
#for executing only Derived class logic(userdefined logic)-->Overiding is required 
#for executing both Base and derived class logic        ---->Super() stmt required.

