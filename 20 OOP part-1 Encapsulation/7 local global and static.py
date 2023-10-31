
#working with static,local and global variables
#global variables------->defined outside the class
#local varibles--------->defined within the class and within the methods.
#static variables------->defined within the class and outside the methods.

r=30     #global variable
class demo:
    x=10  #static variable     
    y=20  #static variable
    print(x)
    print(y)
    print(r)
    def compute(self,p,q):
        #modifying a global variable
        global r   #forward declaration
        r=40
        z=p+q+r          #p,q,z are local variables, here sum of local and global variables.
        w=demo.x+demo.y  #sum of static variables
        print("z=",z)
        print("w=",w)
        print("r=",r)
#end of the class
d1=demo()  #object creation stmt
d1.compute(10,50)
print(r) #global variables
#print(p,q,z,w)  #local variables
print(demo.x,demo.y)


d2=demo()
d2.compute(60,70)
