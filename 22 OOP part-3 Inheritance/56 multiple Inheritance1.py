

#Multiple Inheritence : A derived class with multiple base classes

#Performing intsum,floatsum,boolsum  in derived class by taking features from
#multiple base classes.
class A:
    x=10
    y=20
    def m1(self):
        print("x=",A.x)
        print("y=",A.y)
class B:
    a=3.5
    b=4.7
    def m2(self):
        print("a=",B.a)
        print("b=",B.b)
class C:
    p=True
    q=False
    def m3(self):
        print("p=",C.p)
        print("q=",C.q)
        
class D(A,B,C):
    def m4(self):
        intsum=D.x+D.y
        floatsum=D.a+D.b
        boolsum=D.p+D.q
        print("Integer sum =",intsum)
        print("Float sum=",floatsum)
        print("Bool sum=",boolsum)
d1=D()
d1.m1()
d1.m2()
d1.m3()
d1.m4()

print(D.__bases__)
print(C.__bases__)
print(B.__bases__)
print(A.__bases__)



        


        
    
