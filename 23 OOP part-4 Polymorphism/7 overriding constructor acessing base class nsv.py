
class A:
    def __init__(self):
        self.x=10
        print("from constructor A.....")
class B(A):
    def __init__(self):
        self.y=20
        print("from constructor B.....")
a1=A()
print(a1.x)

b1=B()
print(b1.y)

#print(b1.x)#invalid , bcoz constructor overridden, here x is not initialized

#using derived class object accesing both base and derived class NSV's ,for that the
# solution is by using super()method.
