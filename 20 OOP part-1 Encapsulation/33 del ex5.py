

  #del keyword is not for removing object,it is used to decrease the reference count by 1
#when RC=0,garbage collector is called and destructor executed

class test:
    def __init__(self):
        print("constructor called")
    def __del__(self):
        print("destructor called")
t1=test()#Rc=1
print(t1)
del t1   #Rc=0,garbage collector is called and destructor executed and object removed
#print(t1)
t2=test()#Rc=1
print(t2)
t3=t2    #Rc=2
print(t3)
del t2  #RC decreased to 1 ,Rc=1
#print(t2)
print(t3) #object still available and its address is stored in t3 variable
del t3  #RC decreased to 0,destructor executed and object is removed
#print(t3)#object is not available

#Q)if object R.C=3 then how ref variables?------------------------------->3
#Q)if 3 ref variables storing address of single object----->R.C=?-------->3


#Q)if there are 5 objects---------> 
#max no of times a constructor executes is--------------->5
#min no of times a constructor exectes is---------------->5
#max no of times a destructor executes is---------------->5
#Min no of times a destructor executes is --------------->0
