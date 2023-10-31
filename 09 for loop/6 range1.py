#range(n):for generating range of values from 0 to n-1
#ex:  range(10)--->Generates range of values from 0 to 9

x=range(10)

print(x)
print(type(x))
print(id(x))

#Accessing each element using for loop
for p in x:
    print(p)

#ex:2
y=range(10,20)

for q in y:
    print(q)

#ex:3
z=range(20,30,2) #(startvalue,stopvalue,stepvalue)
for r in z:
    print(r)

#ex:4
w=range(40,30,-1)
for s in w:
    print(s)









    
