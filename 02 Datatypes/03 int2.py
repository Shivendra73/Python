
#case 2: Defining 2 variables with 2 different values--->2 objects are created with 2 different addresses

x=10
y=20

print(x)
print(id(x))
print(type(x))

print(y)
print(id(y))
print(type(y))

z=x+y
print(z)
print(id(z))
print(type(z))

w=y-x
print(w)
print(id(w))
print(type(w))


