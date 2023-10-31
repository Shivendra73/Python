
class x:
    def m1(self,a):
        print("from base class....")
        self.p=a
class y(x):
    def m1(self):
        print("from derived class....")
y1=y()
y1.m1(10) 
y1.m1()


#Here error bcoz method overloading happens which is not supported.



