#Default Constructor

class sample:
    def __init__(self): #constructor
        print("constructor of sample class")
        self.x=10 #constructor initializing 2 NSV's
        self.y=20
        
    def display(self):  #method
        print("method of sample class")
        print(self.x)
        print(self.y)
#end of the class       
s1=sample()#whenever object created ,immediately constructor gets executed automatically
print(s1)
print(s1.x)
print(s1.y)
s1.display()
s1.display()#method called for multiple times

print("\n\n")
s2=sample()   #again constructor executes automatically
print(s2)
print(s2.x)
print(s2.y)
s2.display()
s2.display()

#In this program as there are 2 objects , so constructors executed for 2 times
#if there are 'n' objects then constructor will executed for 'n' times
