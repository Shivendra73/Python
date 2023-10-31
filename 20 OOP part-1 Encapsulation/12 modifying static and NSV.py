

#program for modifying static and non-static variable
class sample:
    a=4.5#static variable
    b=2.6#static variable
    def display(self):
        self.x=10 #non-static variable
        self.y=20 #non-static variable
        print("x=",self.x) 
        print("y=",self.y)
        print("a=",sample.a)
        print("b=",sample.b)
        #modifying the values
        self.x=self.x+50
        self.y=self.y+60
        sample.a=sample.a+70
        sample.b=sample.b+80
        print("x=",self.x) 
        print("y=",self.y)
        print("a=",sample.a)
        print("b=",sample.b)
#end of the class        
s1=sample() #object creation stmt
print(s1) #prints indirect address of object
s1.display() #using object accessing class member x=10 y=20 a=4.5 b=2.6
                                                # x=60 y=80 a=74.5 b=82.6  

s2=sample() #creating 2nd object
print(s2)
s2.display()        #x=10 y=20 a=74.5 b=82.6
                    #x=60 y=80 a=144.5 b=162.6
print(s2.x)
print(s2.y)

s3=sample() #Creating 3rd object
s3.display()   #x=10 y=20 a=144.5  b=162.6
               #x=60 y=80 a=214.5  b=242.6
#Note: For Non-static variables values will be re-initialized for every object
#      but for static variables it takes the old modified values ,here object to
#      object it wont be re-initialised.

      
        
