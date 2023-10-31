

while developing web applications, most of the classes are pre-defined classes,
so we define a user-defined class which extends pre-defined class and overrides the methods
of that pre-defined class

x=10       #here x stores address but not 10
print(x)   #here it wont print address, it prints the value 10---->why? 
print(type(x))

class object:
    def __hash__(self):
        ............#generates hashcode(address)
        ............#here it has got code to print hash code value(address)
        ............

class int(object):
    def __hash__(self):
        ............
        ............#here it wont print hashcode value, bcoz here
        ............it is overriden with diferent code
                     here the method has got code to print the content
                     but not hash code(address)
    
