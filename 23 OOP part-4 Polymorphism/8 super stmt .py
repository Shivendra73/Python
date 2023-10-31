

#Accessing NSV of super class constructor from sub class constructor

class A:
    def __init__(self):
        self.x=10
        print("from constructor A.....")
        print(self)
        
class B(A):
    def __init__(self):
        super().__init__()
        self.y=20
        print("from constructor B.....")
        print(self)


b1=B()
print(b1)
print(b1.x) # now it can be accessed    
print(b1.y)




