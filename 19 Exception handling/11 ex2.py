#ZeroDivisionError
try:  
    a = int(input("Enter a:"))  
    b = int(input("Enter b:"))
    
    if(b==0):  
        raise ZeroDivisionError 
    else:  
        print("a/b = ",a/b)
        
except (ValueError):
    print("Enter Numerical values only")
        
except(ZeroDivisionError):  
    print("The value of b cannot be 0")

finally:
    try:
        print("a=",a)
        print("b=",b)
    except:
        print("Invalid Input")
