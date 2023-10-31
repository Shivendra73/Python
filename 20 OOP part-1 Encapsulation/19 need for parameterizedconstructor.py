
#drawback of default constructor
class sample:
    def __init__(self):
        self.x=0
        self.y=0
s1=sample()
print(s1.x)#printing default values of x and y
print(s1.y)
s1.x=10 #modifying x and y values
s1.y=20
print(s1.x)
print(s1.y)
print("\n\n\n")

s2=sample()
print(s2.x)#printing default values of x and y
print(s2.y)
s2.x=30 #modifying x and y values
s2.y=40
print(s2.x)
print(s2.y)

#Here the problem is for every object s1,s2,s3,s4......sn ,initially initialized
#with default values 0 and 0 and then later assigned or modified with some values,
#but initially only i want 10,20 for s1 and 30,40 for s2,
#so in this case,we go for parameterized constructor.




