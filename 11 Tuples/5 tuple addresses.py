#Working with tuple addresses
#ex1: Lists with same content
x=[10,20,30,40,50]
y=[10,20,30,40,50]

print(x,id(x))
print(y,id(y))

print(x is y) #Compares the address
print(x == y) #Compares the content
#-------------------------------------------------------------------------------------------
#ex:2 Tuples with same content
a=(10,20,30,40,50)
b=(10,20,30,40,50)

print(a,id(a))
print(b,id(b))

print(a is b) #Compares the address
print(a == b) #Compares the content

#Note: 2 Mutable objects with same content always returns 2 diff objects with
#      2 diff addresses' but immutable objects with same content returns only
#      one object with only one address.
#------------------------------------------------------------------------------------------
#ex:3
x=([10,20,30,40,50])
y=([10,20,30,40,50])

print(x,type(x),id(x))
print(y,type(y),id(y))


print(x is y) #Compares the address
print(x == y) #Compares the content

#------------------------------------------------------------------------------------------
#ex:4
x=[(10,20,30,40,50)]
y=[(10,20,30,40,50)]

print(x,type(x),id(x))
print(y,type(y),id(y))
print(x is y) #Compares the address
print(x == y) #Compares the content

#---------------------------------------------------------------------------------------------
#ex:5
p=((10,20,30),(40,50,60),[70,80,90])
q=((10,20,30),(40,50,60),[70,80,90])
print(p,type(p),id(p))
print(q,type(q),id(q))
print(p is q)
print(p == q)

#Note: 2 Tuples with same content--------->only one object is created
#but if the tuples contain list or set or dictionary within it---->diff objects will be created---
#with diff addresses
#----------------------------------------------------------------------------------------------
#ex:6
print(p[0][0],type(p[0][0]),id(p[0][0]))
print(q[0][0],type(q[0][0]),id(q[0][0]))
print(p[0][0] is q[0][0])

a=10
print(a is p[0][0])

x=[10,20,30]
print(x,len(x))

print(x[0] is p[0][0])



















