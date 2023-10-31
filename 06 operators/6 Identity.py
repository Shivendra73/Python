

#Identity operators: These operators are used to compare the addresses of 2 objects
#Identity operators are
#1.is
#2.is not

#ex:1
x=10
y=20

print(x,id(x))
print(y,id(y))

print(x is y)  #Compares the address
print(x == y)  #Compares the content
print(x is not y)

#ex:2
a=10
b=10

print(a,id(a))
print(b,id(b))

print(a is b)
print(a == b)
print(a is not b)

#ex:3
x=[10,20,30,40,50]
y=[10,20,30,40,50]

print(x,id(x))
print(y,id(y))

print(x is y)
print(x == y)

x[1]=25
print(x)
print(y)





















