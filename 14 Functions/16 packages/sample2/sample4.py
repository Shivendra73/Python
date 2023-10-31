import test.demo.samp1 as s1
import test.demo.samp2 as s2
import test.samp3 as s3
import math as m

w=s1.x+s2.y+s3.z

def display4():
    s1.display()
    s2.display2()
    s3.display3()
    print("w=",w)
    print("pi=",m.pi)
    print("sqrt=",m.sqrt(16))
display4()
    
