class sample:
    x=10 #Static variables
    y=20 # "     "
    def display(self):  #A method should always have self as a parameter and whichever object calls 
        print(sample.x) #this method then that object address is stored by self
        print(sample.y)#A SV is always accessed by using a classnmae
        print(self)
#end of the class

#To access the classmembers,create object
#object creation stmt
#objname=classname()
s1=sample() #object creation stmt , here internally a object is created and its address is
            #stored in a variable called reference variable(s1)
print(s1)
#now using this object we can access the methods and variables
s1.display() #here the s1 address will be stored in the self of display()

#printing sV's from outside the class
print(sample.x)
print(sample.y)

s2=sample()
print(s2)

s2.display()














