#Types of Function Arguments:5 Types
'''
1.Non-Default Arguments
2.Default Arguments
3.Keyword Arguments
4.Non-keyword Arguments
5.Arbitrary/Variable length Arguments
'''

#1.Non-Default Arguments: Arguments specified in the function definition and Argument values
#                          compulsorily we need to specify in the function call.


def display(name,age):  #Non-default arguments
    print(name,age)

display("Ajay",25)

#2.Default arguments: Arguments specified in the function definition with some default values
#                     It is not compulsory to specify within the function definition,
#                    if not specified in the function definition, then these default values
#                    are considered.

def show(name="Rahul",age=30):
    print(name,age)

show()
show("Amith")
show("Miller",35)






















