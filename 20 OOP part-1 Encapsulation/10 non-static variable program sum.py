#program illustrating non-static variable(NSV)

class sum:
    a=10
    
    def display(self): #here each object address is passed to self  
        self.x=10 #non-static variable
        self.y=20 #non-static variable
        print("x=",self.x) #accessing and printing non-static variable
        print("y=",self.y)
        print("a=",sum.a)
        print("sum=",self.x+self.y+sum.a)
        print(self)
s1=sum() #creating ref variable s1 which stores indirect address of object.
print(s1) #prints indirect address of object s1
s1.display() #using object accessing class members
             #here s1 address is stored in the self of display and using
             #that self address we are initializing the NSVs.
print(s1.x)#acessing NSV from outside the class using object
print(id(s1.x))
print(s1.y)
print(id(s1.y))
s1.x=30  #Modifying the NSV
print(s1.x)
print(id(s1.x))

s2=sum() #creating 2nd object
print(s2)
s2.display()
print(id(s2.x))
s2.x=40
print(s2.x)
print(id(s2.x))

print(s1.x)
print(s2.x)
print(s1.y)
print("sum=",s1.x+s2.x)

print(s2.x)
print(s2.y)
print("sum=",s2.x+s2.y)


#static variables related to class
#non-static variable related to object
#NSV can be accesed within the class using self.
#NSV can be accessed from outside the class using object/ref.variable

#SV can be accesed inside/outside the class using classname
'''
1.How to define NSV----->within the class within the method using------>self
2.How to access NSV within the class------>self
3.How to access NSV from outside the class------>ref.variable/object
4.who initializes the NSV----------------------->object
5.if there are 2 objects
  how many times memory allocated to NSV-------->2 times
6.does every object has its own NSV's ---------->yes

==q)why NSV should be defined within the method?
q)what happens if we define NSV outside the method?

q)how NSV's and objects are related?

Ans: object address------>passed to self of a method---->using that self only NSVs are created and initialized
     If NSV defined outside the method, the non-static variable cannot get the address of the object--
      -> and NSV cannot be created
'''



