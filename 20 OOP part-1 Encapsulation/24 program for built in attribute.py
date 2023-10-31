#program illustrating built-in attributes
class test:
    """sample class for built-in attribute"""
    x=10
    y=20
    def m1(self):
        print(test.x)
        print(test.y)

t1=test()
t1.m1()
print(test.__bases__)
print(test.__doc__)
print(test.__name__)
print(test.__module__)
#print(test.__dict__)

#Note: we can also add attributes to the class and also add attributes to the object.
#also remove attributes from the class and object using static and non-static variables
# we add static variable(sv)---------->to class.
# we add non-static variable(NSV)----->to object.
