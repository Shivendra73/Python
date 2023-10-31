
#creating multiple objects

class test:   
    """sample class"""
    x=100 #static variable
    y=200 #static variable
    def m1(self):
        test.x=test.x+10
        test.y=test.y+20
        print(test.x)
        print(test.y)
    def m2(self):
        test.x=test.x+30 
        test.y=test.y+40
        print(test.x)
        print(test.y) 
#end of class

t1=test() #creating object
t1.m1()# prints x=110 y=220
t1.m2()# adds 30 and 40 to modified values of x and y,i.e,x=140,y=260 ---->these values stored in a static block

t2=test()#creating one more object,here each object takes value
          #from static block
t2.m1()  #prints  x=150,y=280
t2.m2()  #prints  x=180,y=320





#if u r modifying a static varible, the modified values will be reflected in all
#the methods and objects





