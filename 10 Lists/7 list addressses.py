#working with list addresses:

x=[10,20,30,40,50]
y=[10,20,30,40,50]

print(x,id(x))
print(y,id(y))

print(x is y)
#Note:2 mutable objects with same content returns 2 diff objects with 2 diff addresses
#     2 immutable objects with same content returns only one object with only one address

print(x[0],type(x[0]),id(x[0]))
print(y[0],type(y[0]),id(y[0]))

print(x[0] is y[0])

p=10

print(p is x[0])
