'''complex datatype
A complex no is made up of 2 parts
i)real part--------->float type
ii)imaginary part--->float type'''

x=3+4j
print(x)
print(type(x))
print(id(x))

print(x.real)
print(x.imag)

#we can also create complex no using complex()
x=complex(5,6.3)
print(x)
print(type(x))

y=complex(2,-3)
print(y)

z=complex(1)
print(z)

z=complex()
print(z)

z=complex("5-9j")
print(z)
print(type(z))


