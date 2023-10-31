'''Errors and Exceptions in python:
There are 2 types of Errors:
1)syntax Errors 
2)Run-time errors

1)Syntax Errors :Errors that oocur due to wrong syntaxes like missing colon,missing indentation etc.'''

x=10;y=20
if(x>y):
    print("x is largest")
else:
    print("y is largest")

'''2)Run-time errors: Errors that occur at run-time
  ex:trying to access an element which is not present in a list
  ex:trying to remove an element which is not present in a list'''

x=[10,20,30,40,50]
print(x)
#print(x[8])   #run-time error------>IndexError: list index out of range
#x.pop(7)      #run-time error------>IndexError: pop index out of range
#print(x)
x.remove(70)  #run-time error------->ValueError: list.remove(x): x not in list




  
