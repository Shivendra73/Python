#searching for an element in a set
x={10,20,30,40,50}
print(x,id(x))

print(20 in x)
print(70 in x)
print(70 not in x)

#working with set addresses:
#Note: mutable objects with same content-->multiple objects will be created->
#which have diff addresses
#     Immutable objects with same content->one object will be created----->
#will have same addresses

y={10,20,30,40,50}
print(y,id(y))
print(x is y)  
print(x==y)    

x={10,20,30,40,60}
print(x,id(x))
print(x is x)
print(x==x)

a={1,2,3,4,5}
print(a)

b={1,2,3,4,5}
print(b)
print(a is b)
print(a==b)

m=10
print(m,type(m))

p=100,200,300
print(p,type(p))

a,b,c,d,e=x
print(a,b,c,d,e)
print(a)

m=[10,20,30,40,50]
x1,x2,x3,x4,x5=m
print(x1,x2,x3,x4,x5)

s1=10;s2=20;s3=30
p=s1,s2,s3          
print(p,type(p),len(p))

s1,s2,s3=90,80,70
print(s1,type(s1))
print(s2,type(s2))
print(s3,type(s3))

s1,s2,s3,s4,s5=[100,90.50,75,80,(1,2,3)]
print(s1,s2,s3,s4,s5)
print(s1,type(s1))
print(s2,type(s2))
print(s5,type(s5))

s1=s2=s3=s4=s5=[100,90.50,75,80,92]
print(s1,s2,s3,s4,s5)
print(s1,type(s1),len(s1))
print(s2,type(s2))

x=y=10
print(x,y)

x,y,z=10,20,30
print(x,y,z)

x,y,z=[1,2,3],[4,5,6],[7,8,9]
print(x,y,z)

x1,x2,x3,x4,x5=range(5)  #range(5) -->Generates range of values from 0 to 4
print(x1,x2,x3,x4,x5)


s1,s2,s3,s4,s5=range(50,60,2)
print(s1,s2,s3,s4,s5)



