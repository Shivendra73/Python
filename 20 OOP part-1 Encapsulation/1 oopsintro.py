
OOP:Object-Oriented Programming 

Features of OOP

1.Encapsulation
2.Abstraction
3.Inheritance
4.polymorphism


The above OOP principles provides
security,
flexibility and
re-usability.

 In java,the developer is forced to write programs using oop
 principles only,we cannot develop applications witout OOp in Java
 
 But in python,we can write programs using
 1.Procedural-oriented programming
 2.Object-Oriented programming

------------------------------------------------------------------------------


 1) Encapsulation :- combining data and methods

Q) why we need to combine data and methods?
 
 Every application has got data and operations.
 Data represented using variables
 operations represented using functions/methods.
 
 //customer--->data  //all are global variables
 cname="miller"
 caccno=501234678
 caddr="Ameerpet"
 bal=50000

 //customer operations (functions)
def deposit(damt):
    pass
def withdraw(wamt):
    pass
def transfer(daccno,tamt):
    pass
Note:damt,wamt,daccno,tamt are the local variables to the respective functions.
cname,caccno,caddr,bal are global variables which can be accessed by all the fuctions

damt is a local variable of deposit(),so only deposit() can
access damt, but not by other functions.
so local variables can be executed by only the particular function.

//emp--->data
 ename="James"
 eid=101
 esal=30000
 eaddr="hyd"
//emp operations
def tax():
    pass
def hra():
    pass
def pf():
    pass

in the above example, all the global variables of customer and
emp can be accessed by all the fuctions of customer and emp.

actually-->customer data should be accessed by only customer functions
 and emp data should be accessed by emp functions only but here
customer data is accessed by both customer and emp functions
and similarly emp data is accessed by both customer and emp
functions.so here there is no security,

so we need to make customer data available only to customer functions
similarly we need to make the emp data available only to emp functions.

so we group customer data and customer functions as one group called customer class
   we group emp data and emp functions as one group called as emp class, so that
   only emp functions can access emp data and customer functions can access customer data.

Encapsulation: The process of grouping/binding related data(variables)
along with methods(functionalities) is called as encapsulation.

Encapsulation is implemented by using a class.
------------------------------------------------------------------------------

Class: A class is a structure which groups/binds the related
data along with its methods.

A class is a collection of variables and methods.

Data is represented using variables and
operations are represented using methods.

In class,we can have 2 types of variables,
1.Static variables
2.Non-static variables

syntax of class :
    class classname:
        """doc string"""   -->says about the functionality of  a class
        ----------------
        ----------------
        ---------------- -------->data(variables)+methods
        ----------------
        ----------------
Note: All the stmts within the class should follow the indentation.

A class consists of the following:
    1.Doc string (optional)
    2.Variables
       i. static variables
       ii.Non-static variables
    3.Methods

cname,-----------------
caddr,
caccno
cbal                   --------->customer group,
deposit()                        consisting of data(variables)
transfer()                       such as cname,caddr,caccno,cbal and
withdraw()-------------          methods such as deposit(),transfer() and withdraw()
                                 

ename------------------
eid
esal
design                ----------->emp group
TA()
DA()
HRA()
PF()-------------------

in the above example,we have got 2 groups,

customer group and emp group, we can represent by 2 classes
class customer:
    .........
    .........
    .........-------->consists of customer variables + customer methods(functions)
    .........

class emp:
    .........
    .........
    .........-------->consists of emp variables + emp methods
    .........
    .........

in class customer, customer variables can be accesssed only by customer methods
similarly,in emp class, emp variables can be accessed only by emp methods.

--------------------------------------------------------------------------------------------------
object: An object is an instance of a class                          
A class is a collection of similar objects.
we can create 'n' no of objects for a class
each object will have its own copy of variables and methods.

ex:
class emp:
    eid=input("Enter Eid:")
    ename=input("Enter Ename:") 
    sal=input("Enter sal:")
    desig=input("Enter Designation:")
    def tax():
        pass
    def hra():
        pass
object--->e1=emp()
object--->e2=emp()

Here e1,e2 are the objects of the class emp which uses the same class structure
-----------------------------------------------------------------------------------

2)Abstraction: Hiding up of data and methods of a  class.
ex: properties of one class cannot be accessed by another
class.
if customer class is given to a bank,then for 'n' no of
customers, only one class is created or used, but 'n' no of
objects are created for the customer class such as c1,c2,c3...


-------------------------------------------------------------------------------------------------

3)Inheritance: Inheritance is the process of acquiring the properties of one class into anther class.

 Inheritance can be achieved by deriving a new class from
 existing class.The new class will get the combined features
 of both the classes.
-----------------------------------------------------------------------------

4)Polymorphism: The ability to take more than many forms.

 An operation which exhibits diferent behaviours at different
 instances.

 poly means many
 morphism means multiple logics or functionalities to perform an operation

-----------------------------------------------------------------------------
 

























 

    






















 




 


 
