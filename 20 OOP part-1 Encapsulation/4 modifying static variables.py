
#Defining multiple methods within the class 
#modifying the values of static variables using a method

class test:   
    """sample class"""
    x=10 #static variable
    y=20 #static variable
    def m1(self):
        print(test.x)#s.v accessed using classname 
        print(test.y)
        #modifying values of x and y
        test.x=30
        test.y=40 #these changes are affected in other method also
    def m2(self):
        print(test.x)
        print(test.y)
#end of class

t1=test() #object creation stmt ,here internally object is created and its
          #address is stored by a variable called reference variable(t1)
t1.m2()
t1.m1()#prints the values of x and y and modifies the values
t1.m2()#prints the modified values.
t1.m1()

#Static variables are no way related to objects
#Static variables always takes the modified values

#Note: If u modify a static varible then the changes will be reflected in all
#the methods and objects
#always the modified or updated static variable value will be considered

t2=test()  #creating another object
t2.m2()
t2.m1()
#modifying SV's from outside the class
test.x=50  #Modifying SVs from outside the class
test.y=60

print("x=",test.x)
print("y=",test.y)
t1.m2()
t1.m1()
t1.m2() 

