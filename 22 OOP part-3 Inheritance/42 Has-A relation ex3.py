
class x:
    a=10
    def __init__(self):
        self.b=20
        print("constructor......")
    def m1(self):
        print("from m1....")
        
class y:
    c=30
    def m2(self):
        print("from m2....")
    def display(self):
        self.d=40
        print(x.a)#Accessing SV of class x using classname
        self.x1=x() #creating ref_variable of x  #here self.x1 is NSV which can be used in
                    #other methods
        print(self.x1.b)#Accessing NSV of class x using ref_variable
        print(self.x1)
        print(y.c)#Accessing sv of class y
        print(self.d)#Accessing NSV of class x  
        #we cant access m1()method of class x using self bcoz,
        #self stores address of current class object,so to access m1()
        #of class x,create object of class x and using that ref_variable
        #we can access m1()
        self.x1.m1()#Accessing m1() of class x using ref_variable
        self.m2()#Accessing m2() of class y using self
    def show(self):  
        print(self.x1.b)
        self.x1.m1()
        
y1=y()
print(y1)
y1.display()
y1.show()

        
        
        
