

#when sub class object is created,then first constructor
#of super class is executed.

class x:
    def __init__(self):
        print("base class constructor....")
    def m1(self):
        print("from m1.....")
        
class y(x):
    def m2(self):
        print("from m2....")
y1=y()
y1.m1()
y1.m2()
