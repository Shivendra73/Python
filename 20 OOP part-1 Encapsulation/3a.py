#Adding attributes to a class and adding attributes to a object
#Adding static and non-static variables to the class and object explicitly


#Adding static variables to the class explicitly
#Adding Non-static variables to the object explicitly.


class sample:
    a=10
    def display(self):
        self.b=20
#end 0f the class
s1=sample()

#Accessing static variable(a) from outside the class
print("a=",sample.a)

#Adding one more static variable(c) from outside the class
sample.c=30
print("c=",sample.c)

s1.display()
#Accessing NSV(b) from outside the class
print("b=",s1.b)
#Adding one more NSV(d) to the object(s1)
s1.d=50

print("d=",s1.d)










