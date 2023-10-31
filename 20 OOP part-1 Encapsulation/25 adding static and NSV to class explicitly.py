#Adding attributes to a class and adding attributes to a object
#Adding static and non-static variables to the class and object explicitly


#Adding static variables to the class explicitly
#Adding Non-static variables to the object explicitly.

class sample:
    a=10
    def display(self):
        self.b=20

s1=sample()

#Printing sv(a) from outside the class
print("a=",sample.a)

#Adding one more StaticVariable(C) to the class from outside the class
sample.c=30
print("c=",sample.c)

s1.display()
#printing NSV(b) from outside the class
print("b=",s1.b)

#Adding one more Non-static variable(d) to the object(s1) explicitly
s1.d=40
print(s1.d)

#Creating one more object(S2)
s2=sample()
s2.display()
print("b=",s2.b)
#print("d=",s2.d) #invalid bcoz, d is added to s1 object only,s2 cannot access
#adding one more NSV(e) to the object(s2) explicitly
s2.e=50
print("e=",s2.e)
#print("e=",s1.e) #invalid bcoz ,e is added to s2 object only,s1 cannot access

#static variables of the class------->a=10,c=30
#Non-static variables of the class--->b=20,d=40,e=50

#object s1 can access------------->b,d
#Object s2 can access ------------>b,e

#Removing attributes from the class and object using del keyword

#removing static variable(a) from the class
del sample.a

#print("a=",sample.a)  #Error

#removing Non-static variable(d) fron the object(s1)
del s1.d

#print("d=",s1.d)  #Error

#removing Non-static variable(e) fron the object(s2)
del s2.e

#print("e=",s2.e)  #Error

#Note:del can only remove static and non-static variables only but del cannot remove a object.



























        
        
