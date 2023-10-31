

# If I write default except block first,then control won't go to the next except blocks 
# So if I define it first, we get syntax error,
# So always write default except block at the last.

try:
    x=int(input("Enter First No:"))   #10
    y=int(input("Enter Second No:"))  #abc, if error here,remaining stmts of try block r skipped
    z=x/y
    print(z)
    
except:                                #default except block
    print("error occured")
   
except(ZeroDivisionError):
    print("2nd No cannot be zero")
    
except(ValueError):
    print("Enter Numerical values only")









