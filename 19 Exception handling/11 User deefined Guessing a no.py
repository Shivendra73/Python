

#Program to guess a number
class Error(Exception):   #Error is userdefined class that extends pred-defined class Exception
    """Base class for other exceptions"""
    pass
class ValueTooSmallError(Error): #ValueTooSmallError is a userdefined class that extends another
                                  # user-defined class(Error) which extends pre-defined class Exception
    """Raised when the i/p value is too large"""
    pass
class ValueTooLargeError(Error): #ValueTooLargeError is a userdefined class that extends another
                                  # user-defined class(Error) which extends pre-defined class Exception
    """Raised when the i/p value is too small"""
    pass
number=10
while True:     #infinite while loop
    try:
        x=int(input("Enter a Number:"))
        if(x<number):
            raise ValueTooSmallError
        elif(x>number):
            raise ValueTooLargeError
        break
    except(ValueTooSmallError):
        print("This value is too small,try again")
        
    except(ValueTooLargeError):
        print("This value is too large,try again")
print("CONGRATULATIONS!! You Guessed it Correctly...")


"""output:
    Enter a Number:5
This value is too small,try again
Enter a Number:15
This value is too large,try again
Enter a Number:10
CONGRATULATIONS!! You Guessed it Correctly.."""
