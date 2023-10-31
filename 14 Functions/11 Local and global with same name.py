#Local and Global variables with same name

x=10             #Global variable

def display():
    x=20         #Local variable
    print(x)     #Always local variable  wil be given preference over global

def show():
    print(x)
display()
show()
