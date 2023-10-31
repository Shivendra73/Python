
#modifying non-static variables
class sample:
    def __init__(self):
        self.x=10
        self.y=20
    def m1(self):
        self.x=self.x+30 #modifying NSV
        self.y=self.y+40
        print(self.x)
        print(self.y)
s1=sample()# constructor executed automatically,
           #means NSV's are created and initialized

print(s1.x) #x=10
print(s1.y) #y=20
s1.m1()  #  x=40 y=60
s1.m1()  #  x=70 y=100

s2=sample()  #constructor executes for 2nd time
print(s2.x) #x=10
print(s2.y) #y=20
s2.m1()     # x=40 y=60
s2.m1()     # x=70 y=100





    
