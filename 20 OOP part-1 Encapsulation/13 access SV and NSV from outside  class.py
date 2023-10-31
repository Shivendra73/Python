

#program to access static and non-static variables from outside the class
class sample:
    a=4.5
    b=2.6
    def display(self):
        self.x=10 #non-static variable.
        self.y=20 #non-static variable.
#end of the class            
s1=sample() #here no NSV's ,bcoz values will be allocated when method is executed
s1.display()#now values allocated and stored in an object and object in-direct address stored in reference variable 
print(sample.a)#static variable accessed using class name 
print(sample.b)

print(s1.x,type(s1.x))#NSV accessed using reference variable
print(s1.y)#if we execute these 2 stmts without executing s1.display()method
#we get error bcoz, values wont be allocated to x and y,so call s1.display() first.
#but without calling a method, I want NSVs to get initialized,then go for constructors.
#To overcome this, allocate values for NSVs during object creation only using constructor.
        
    

