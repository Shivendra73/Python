

#Implementing try,except and finally

try:
    x=int(input("Enter First No:"))   
    y=int(input("Enter Second No:"))  
    z=x/y
    print(z)


except(ZeroDivisionError):
    print("2nd No cannot be zero") 

finally:    # here prints msg of finally block before terminating abnormally
    print("welcome to Python world!!!")
   
print("end")



#Try the execution for all the 3 cases ,in all 3 cases finally will be executed
