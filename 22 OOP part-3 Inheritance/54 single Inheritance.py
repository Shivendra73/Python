

#Single Inheritence: A derived class with a  single base class

class A:
    def m1(self):
        print("from m1......")
a1=A()
a1.m1()
print(A.__bases__)

#Object class is the base class for all the classes in python

#here A is a derived class with a single base class(object class)

#If a class is not extending any class then by default object class is the base class


