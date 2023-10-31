
#Nested if-else:
#Nested blocks: Blocks withi a block

#To check largest of 3 No's
x=int(input("Enter value of x:"))
y=int(input("Enter value of y:"))
z=int(input("Enter value of z:"))

if(x>y):
    if(x>z):
        print(x,"is the largest!!!")
    else:
        print(z,"is the largest!!!")
else:
    if(y>z):
        print(y,"is the largest")
    else:
        print(z,"is the largest!!!")

