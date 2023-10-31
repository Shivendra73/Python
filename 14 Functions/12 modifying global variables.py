#Modifying the global variables from within the function

x=10

def display():
    global x #Forward declaration,This declaration tells that the global variable value
             #is going to get modified in the later stmts
    x=15
    print(x)
def show():
    print(x)

show()
display()
show()
    
