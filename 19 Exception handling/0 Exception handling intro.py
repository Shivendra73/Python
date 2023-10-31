
Exception Handling:

Generally, there are 2 types of errors in python
1.Syntax errors
2.Run-time errors

1)Syntax errors: The errors that occur due to wrong syntaxes

ex: wrong space indentation
    missing colon
ex:
def display()  #syntax error------>missing colon
print("hello") #syntax error------>wrong indentation
    

Python interpreter checks for syntax errors and then converts source code
to byte code(.pyc) and then converts this byte code to machine code and executes.

If there are syntax errors,then .pyc file wont be generated,
If .pyc file is not generated then the python program wont be executed.

----------------------------------------------------------------------------------------------------------
2)Run-time errors:   Errors that occur at run-time,i.e during the execution of
                     the program.

ex:Trying to access an element which is not present ------>we get Runtime Error
   Trying to remove an element which is not present------->we get Runtime error
 
ex-1:
x=[10,20,30,40,50]
trying to access 10th element---Runtime error
print(x[10])----Runtime error---->IndexError

    ex-2: Trying to remove an element which is not present-----> gives runtime error
 ex: x.remove(90)----->Runtime error---->ValueError

#Run-time errors:

x=[10,20,30,40,50]

#print(x[9])                #IndexError

#x.remove(90)               #ValueError

#print(y)                   #NameError

#y=list(10)                 #TypeError

#z=list("hello","world")    #TypeError


y=(10,20,30,40,50)

#y.append(60)  ---------------->AttributeError

#z.append(70)  -------------->AttributeError

#print("python"+3)          #TypeError

#f=open('sample5.txt')      #FileNotFoundError

x=10
y=0
#z=x/y                        #ZeroDivisionError



#x=int(input("Enter value of x:")) --->"hello" #ValueError

 
whenever we get run-time error,program execution is terminated abnormally

#Abnormal Termination: Termination of the program in middle of the execution without
#executing upto the last stmt

for every run time error,corresponing pre-defined python classes are available,
these classes are called as Exception classes.

Exceptions are the classes,which contain run-time error representations.

#we can see all the pre-defined exeception classes within a module called as __builtins__
print(dir(__builtins__))
when ever we get run-time error,run-time error representation class object
will be created automatically.
whenever this object is created,we say that exception is raised, we need to
handle it with a code,otherwise abnormal termination.



2types of exceptions:
    
Pre-defined Exceptions(Built-in Exceptions)------>Raised automatically and we need
                                                  to handle.
User-defined Exceptions-------------------------->We need to raise and we need to handle.


reasons for run-time errors:
1.Entering invalid input
2.Due to invalid code
3.memory related issues
4.Hardware related problems.





















