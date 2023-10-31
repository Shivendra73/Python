
#program for single inheritence
class A:
    x=10
    def m1(self):
        print("x=",A.x)
        
class B(A):
    y=20
    def m2(self):
        z=B.x+B.y
        print("y=",B.y)
        print("z=",z)
b1=B()
b1.m1()
b1.m2()
print(B.__bases__)
print(A.__bases__)

#here B is a derived class with a sigle base class A
