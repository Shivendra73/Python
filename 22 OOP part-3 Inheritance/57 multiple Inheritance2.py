

# If the base classes have method with same name and using derived class object if you acess the
# method then which base class method will be executed??
class A:
    x=10
    y=20
    def m1(self):
        print("hello from A......")
        print("x=",A.x)
        print("y=",A.y)
class B:
    a=3.5
    b=4.7
    def m1(self):      #same method name of class A
        print("hello from B.....")
        print("a=",B.a)
        print("b=",B.b)

class C(B,A):
    def m2(self):
        intsum=C.x+C.y
        floatsum=C.a+C.b
        print("Integer sum =",intsum)
        print("Float sum=",floatsum)
           
c1=C()
c1.m1()

#here m1 of class A is executed bcoz while inheriting
         #class A is inherited first,i.e we said class C(A,B)
         #but if we say class C(B,A),then m1 of class B executes
c1.m2()


        


        
    
