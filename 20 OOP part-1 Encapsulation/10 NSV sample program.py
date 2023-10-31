#program illustrating NSV

class sample:
    a=10
    def display(self):
        self.x=20
        self.y=30
        print("a=",sample.a)  #accessing a sv within the class using classname
        print("x=",self.x)    #Accesssing a NSV within the class(method) using self
        print("y=",self.y)
        print(self)
    def show(self):
        self.z=40
        print("x=",self.x)
        print("y=",self.y)
        print("z=",self.z)
#end of the class
s1=sample()
print(s1) #prints the object address
#Accesing SV from outside the class using classname
print("a=",sample.a)
s1.display() #without calling a method NSVs cannot be created or initialized
s1.show()
#Accessing NSV's from outside the class using object/reference variable
print("x=",s1.x,type(s1.x),id(s1.x))
print("y=",s1.y)
print("z=",s1.z)

#creating one more object

s2=sample()
print(s2)

s2.display()
s2.show()
print("x=",s2.x,id(s2.x))


#static variables related to class
#non-static variable related to object
#NSV can be accesed within the class using self.
#NSV can be accessed from outside the class using object/ref.variable

#SV can be accesed inside/outside the class using classname
'''
1.How to define NSV----->within the class within the method------>self
2.How to access NSV within the class------>self
3.How to access NSV from outside the class------>ref.variable/object
4.who initializes the NSV----------------------->object
5.if there are 2 objects
  how many times memory allocated to NSV-------->2
6.does every object has its own NSV's ---------->yes

==q)why NSV should be defined within the method?
q)what happens if we define NSV outside the method?

q)how NSV's and objects are related?

Ans: object address------>passed to self of a method---->using that self only NSVs are created and initialized
     If NSV defined outside the method, the non-static variable cannot get the address of the object--
      -> and NSV cannot be created
'''











        
