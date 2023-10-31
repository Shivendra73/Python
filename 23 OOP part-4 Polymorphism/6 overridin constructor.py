#overriding a constructor

class x:
    def __init__(self):
        print("from constructor of x....")
        
class y(x):
    def __init__(self):
        print("from constructor of y....")
y1=y()


#if u want super class constructor to be executed, then create object of super class
x1=x()  

