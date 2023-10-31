
#Program illustrating all types of variables---->local,global,static and non-static
x=10            #global variable
class test:
    y=20        #static variable   
    def display(self,p): #local variable
        self.z=p       #non-static   
        self.w=x+test.y+self.z+p
        print("x=",x)  #printing global variable
        print("p=",p)  #printing local variable
        print("y=",test.y) #printing static variable
        print("z=",self.z) #printing non-static variable
        print("w=",self.w) #printing non-static variable

#end of the class
t1=test()
t1.display(30)
print(x)
print(test.y)
print(t1.z)
print(t1.w)
#print(p)  # local variable cant be accessed


#Local variable can be accessed only by that method but NSV can be accessed by
#all the methods of a class and also by the other classes.

