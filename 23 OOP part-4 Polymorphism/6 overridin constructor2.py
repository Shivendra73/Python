

class x:
    def __init__(self,a,b):
        print("from constructor of x....")
        self.x=a
        self.y=b
        print("x=",self.x)
        print("y=",self.y)
        
class y(x):
    def __init__(self):
        print("from constructor of y....")
        
y1=y()
y2=y(10,20)
#x1=x(10,20)


#constructor oveloading happens---------->error
