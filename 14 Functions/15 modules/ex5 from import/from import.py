'''
Types of imports :2 types

1)Normal import: Everytime when we import a property from a module then compulsorily we need to
                 specify the modulename before the propertyname
                 ex:  mod1.x
                      mod1.display
                      math.pi
                      math.sqrt


2)from import : Here no need to specify the modulename before the propertyname ,here directly
                we can import the properties

'''
#ex:

from mod1 import *
from mod3 import *
from math import *

z=x+y

def compute():
    display()
    show()
    print("z=",z)
    print("pi=",pi)
    print("sqrt=",sqrt(16))
compute()





    

                
                
