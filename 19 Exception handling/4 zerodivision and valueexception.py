
#Single try with multiple except blocks:

#In order to handle different exceptions by using different except blocks,
#then we go for
#single try with multiple except blocks. 

#ValueError

#x=int(input("Enter First No:")) --->"hello" (we get valueerror),
#so keep these stms in try block.  

try:
    x=int(input("Enter First No:"))   #10
    y=int(input("Enter Second No:"))  #hello, if error here,remaining stmts of try block r skipped
    z=x/y
    print(z)
    #print(w)
    
except(ZeroDivisionError):
    print("2nd No cannot be zero")
    
except(ValueError):
    print("Enter Numerical values only")

except(NameError):
    print("variable is not defined")

except:                             #default except block
    print("error occured")

#-ValueError except block can handle only one exception.

#ZeroDivisionError except block can handle only one exception
    
#-default except block can handle any type of exception.

#-In default except block,we can display only common user-friendly error msg
#  but here we cannot display the corresponding exception related user-friendly error message.

#-In the above program, if exception is raised in the try block,then control will
#go to 1st except block,if 1st except block has handled that exception,then control
#will not go to remaining except blocks
    
# - If 1st except block has not handled that exception,then only control will go to
#    the next except block,still not handled,control goes to default except block.


#in try block, if error in 1st line only,then remaining stmts will be skipped in try block
# and control goes to except block, so in try block, only one exception it can handle '''
    



    
