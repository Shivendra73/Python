# ex of method overriding
class RBI:
    x=10
    def minbalance(self):
        minbal=0
        print("MINBAL:",minbal)

class HDFC(RBI): # here minbal=1000,i wont follow RBI min bal here,so i doesnt want super class method 
    def minbalance(self):   # logic to execute, so i overide the method so that sub class  
        minbal=1000         # method logic executes
        print("HDFC MINBAL:",minbal)
        
class ICICI(RBI):
    x=100
    def minbalance(self):
        minbal=2000
        print("ICICI MINBAL:",minbal)

class SBI(RBI):
    x=10
    pass #here i doesn't want tooveride, i will follow RBI rules only
        #here i will execute super class method logic only
h1=HDFC()
h1.minbalance()

i1=ICICI()
i1.minbalance()

s1=SBI()
s1.minbalance()

print(RBI.x)
print(ICICI.x)
print(SBI.x)




