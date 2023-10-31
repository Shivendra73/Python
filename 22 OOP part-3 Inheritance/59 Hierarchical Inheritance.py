

#Hierarchical Inheritence: A base class with multiple derived classes

class Arith:
    x=20
    y=10
    def m1(self):
        print("x=",Arith.x)
        print("y=",Arith.y)
        
class Add(Arith):
    def m2(self):
        sum=Add.x+Add.y
        print("sum=",sum)
        
class Sub(Arith):
    def m3(self):
        diff=Sub.x-Sub.y
        print("Diff=",diff)
        
class Mul(Arith):
    def m4(self):
        prod=Mul.x*Mul.y
        print("product=",prod)
        
class Div(Arith):
    def m5(self):
        div=Div.x/Div.y
        print("Division=",div)
a1=Add()
a1.m1()
a1.m2()

s1=Sub()
s1.m3()

m1=Mul()
m1.m4()

d1=Div()
d1.m5()

print(Div.__bases__)
print(Mul.__bases__)
print(Sub.__bases__)
print(Add.__bases__)
print(Arith.__bases__)












        


