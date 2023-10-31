#case 4:initializing multiple values to a variable---> multiple objects created--->always latest value will be returned.

x=10
print(id(x))

x=20
print(x)
print(id(x))
print(type(x))

x=10
print(x)
print(id(x))
print(type(x))
