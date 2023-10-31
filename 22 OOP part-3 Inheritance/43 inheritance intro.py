

Is-A relationship, we can implement  in python by using inheritance
Here without classname or ref_variable name or modulename,we can use
the properties of one class in another class.

Inheritance:

Inheritance:The Concept of making available the properties of one class
            to another class is called inheritance.

            
Inheritance is nothing but deriving a new class form existing one.
The derived class will have the combined features of both the existing and new class.


The existing class is called as base class or super class or parent class
The new class is called as derived class or sub class or child class.


Base class or super class is a class from which new classes can be created.
Derived class or sub class is a class that inherits or extends the features
of base class.

                    (or)
A class which is extended by another class is known as a super class or base class.
A class which is extending another class is known as sub class or derived class.


ex:
class A:
    a=10
    b=20
    def m1(self):
        pass
class B(A): #class B extending class A  (Inheritance)
    c=30
    d=40
    def m2(self):
        pass
#There are 2 variables(a,b) and 1 method(m1) in class A.
#There are 4 variables (a,b,c,d) and 2 methods(m1,m2) in class B.
#class B extending class A,means class B has combined features of both the classes 
#class B(sub class) can access all the properties(a,b,m1()) of super class A


    
    

    
    






        
