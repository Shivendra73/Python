
#Removing attributes from a class and object.
#Removing SV , NSV ,object
class sample:
    x=10
    y=20
    def m1(self):
        self.a=40
        self.b=50
s1=sample() #RC=1
print(s1)
print(sample.x)
print(sample.y)
#removing both the static variables
del sample.x #removing attributes of a class
del sample.y #removing attributes of a class
print(s1)
#print(sample.x)
#print(sample.y)

s1.m1()
print(s1.a)
print(s1.b) 
#removing the NSV's

del s1.a  #removing attribute(NSV) of object
#print(s1.a)
print(s1)
del s1.b  #removing attribute(NSV) of object
#print(s1.b)
print(s1)

del s1 # R.c=0 and object removed
#print(s1)


s2=sample()
s2.m1()
print(s2.a)
print(s2.b)
