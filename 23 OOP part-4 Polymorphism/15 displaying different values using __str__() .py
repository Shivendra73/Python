
#dispalying different values for different objects ---->by using parameterized constructor

#i.e displaying dynamic content

#object1----->one value
#object2----->another value

class x:
    def __init__(self,a):
        self.p=a
    def __str__(self):
        return self.p
x1=x("Ajay")
print(x1)
print(x1.__str__())

x2=x("pranay")
print(x2)
print(x2.__str__())

'''
Q)what happens internally whenever a derived class object is created?

Ans: first creates objects of base classes follwed by derived class,
     all these objects are stored in the same memory location , this address
     is taken by python interpreter and using object class __hash__() method
     generates hash value (in-direct address) which is converted into
     hexadecimal format by __str__() method.This in-direct address is stored
     within derived class ref. variable

    That's why using derived class ref.variable we can acces all the properties
    of base and derived classes.
'''









     
