

#program illustrating Has-A relationship(using classname or ref_variablename)
#without inheritance
class A:
    x=10
    def __init__(self):
        self.y=20
    def m1(self):
        print("from m1......")


class B:
    z=30
    def m2(self):
        print(A.x)#Accessing sv of another class using classname
        a1=A() #object creation stmt for class A
        print(a1.y)#Accessing NSV of another class using ref_variable
        a1.m1()#Accessing method of another class using ref_variable but not with using self
        print(B.z)
        sum1=A.x+a1.y+B.z
        print("sum=",sum1)
b1=B()
b1.m2()
        
        
