# case 3: defining 2 variables with same values----->only one object created and its address is returned to both variables

x=10

y=10

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
