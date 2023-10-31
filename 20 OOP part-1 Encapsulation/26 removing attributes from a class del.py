Removing attributes from a class:
Removing attributes from a object:

ex:
    del test.a     #removing a static variable
    del t1.b       #removing a non-static variable
    here del can remove only static and non-static variables but del cannot remove a object
    
 del:del is a keyword,which is used to decrease the reference count of an object.
     
Reference count:No of variables pointing to an object will give the reference count.
(or) no of variables storing the address of an object will give the reference count.

 ex:1
     class test:
         pass

     t1=test() #here the variable t1 pointing to an object, so R.C=1
     del t1    #means it decreases the reference count by 1,so R.C=0
               #whenever any object reference count(R.C) becomes zero
            then that object is removed automatically by the garbage collector
            whenever object is going to be deleted,then Destructor is called.
            i.e when RC becomes 0.

 ex:2
     class test:
         pass

     t1=test()
     t2=t1  #here 2 variables(t1,t2) are pointing to same object,so RC=2
            #here t1 and t2 storing address of same object.

     del t1 # Rc decreases to 1,i.e RC=1  ,object is not removed,destructor not called
     del t2 # RC becomes 0,i.e RC=0 ,gargabge collector removes that object and destructor executed.


#Notes:
No.of Ref.Variables == no of Objects-------------------->False
RefCount == No of Ref.variables pointing to a object---->True
RefCount == No of Objects ------------------------------>False


     




     




    
     
     

         
