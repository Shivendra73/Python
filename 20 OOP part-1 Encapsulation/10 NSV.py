
class sample:
    a=10  #static variable
    b=20
    def display(self):
        self.x=30
        self.y=40
        print("a=",sample.a)  #Accessing SV within the class
        print("b=",sample.b)
        print("x=",self.x)    #Accessing NSV from within the class using self
        print("y=",self.y)
    def show(self):
        print("x=",self.x)
        print("y=",self.y)
#end of the class
s1=sample() #here internally object gets created and its address is taken by python intertpreter
            #and generates in-direct address and this in-direct address is stored in a
            #variable called as reference variable(s1)


print("a=",sample.a) #Accessing SV's from outside the class using classname
print("b=",sample.b) #   "                 "                         "
s1.display()         #Here s1 address is stored in self of display and using that
                     #self only NSV's x and y are displayed
print("x=",s1.x)     #Accessing NSV's from outside the class using ref.variable/object
print("y=",s1.y)         
