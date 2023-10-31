
#Multi-level Inheritence: Deriving a class from another derived class
m=45
class A:
    x=10
    y=20
    print("m=",m)
    def m1(self):
        global m #forward declaration
        m=55
        print("m=",m)
        print("x=",A.x)
        print("y=",A.y)

class B(A):
    z=30
    def m2(self):
        global m
        m=60
        total=B.x+B.y+B.z
        print("z=",B.z)
        print("total=",total)
        print("m=",m)
class C(B):
    def m3(self):
        avg=(C.x+C.y+C.z)/3
        #print("Total=",C.total)
        print("Avg=",avg)
        print("m=",m)
        
c1=C()
c1.m1()
c1.m2()
c1.m3()
#print("total=",c1.total)
print("m=",m)

print("\n\n\n\n")
b1=B()
b1.m1()
b1.m2()

a1=A()
a1.m1()

print(C.__bases__)
print(B.__bases__)
print(A.__bases__)







