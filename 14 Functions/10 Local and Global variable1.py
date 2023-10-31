#Local and Global variables

#Local variables: Variables defined within the function and accessed only within the function

#Global variables:Variables defined outside the function and can be accessed by all the functions

x=10              #Global variable
def display():
    y=20          #Local variable
    print(x)
    print(y)

def show():
    print(x)
    #print(y)

display()
show()
