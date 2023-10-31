class test:
    def __init__(self):
        print("constructor called")
    def __del__(self):
        print("destructor called")  
t1=test() #Rc=1
t2=t1     #RC=2
t3=t1     #RC=3,all 3 variables pointing to same object,storing address of same object,so RC=3
print(t1)
print(t2)
print(t3)

t1=test() # here previous object RC decreases by 1 i.e Rc becomes 2 
          # previous t1 variable removed and a new t1 variable is created
          #which will point to another object
          #so first object RC becomes 2,bcoz one variable t1 is removed
print(t1)#prints new object address

t2=test() #previous t2 variable removed and a new t2 variable is created
           #which will point to another object
         #so first object RC becomes 1,bcoz  t2 is removed
print(t2)#prints new object address

t3=test() #previous t3 variable removed and a new t3 variable is created.
        #which will point to another object
         #so first object RC becomes 0,bcoz t3 is removed as Rc=0,object gets removed  and destructor is called
print(t3)#prints new object address

del t1
del t2
del t3




