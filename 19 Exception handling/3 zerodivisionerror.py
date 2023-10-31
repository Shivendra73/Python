x=int(input("Enter First No:"))
y=int(input("Enter Second No:"))
try:
      z=x/y                          #stmts which causes exception are kept within try block
      print(z)

except(ZeroDivisionError):           #exception object assigned to corresponding error-representation class
     print("2nd No cannot be zero") # we can display user friendly error messages     

#except Exception as e:
#      print(e)



