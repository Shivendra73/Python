
#object class:object class is the super class for every class in python.

#object class is a pre-defined(built-in)class,which is defined in __builtins__ module

#If a class is not extending any other class,then by default that class
#internally extends object class.

class A:
    pass
class B(A):
    pass
class C(B):
    pass
class D:
    pass

print(B.__bases__) #to know the base class of B
print(A.__bases__) #to know the base class of A, by default i.e object class
print(C.__bases__)
print(D.__bases__)
#help(object)       #to know about object class
#print(dir(object)) #to know the properties of object class
#help(object.__hash__)# to know the hash value of object class


