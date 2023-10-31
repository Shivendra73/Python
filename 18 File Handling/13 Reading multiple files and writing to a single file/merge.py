#List functions:

x=[30,10,40,20,50]
print(x)

print(type(x))
print(id(x))
print(len(x))
print(sum(x))
print(max(x))
print(min(x))
avg=sum(x)/len(x)
print("Avg=",avg)
print(sorted(x))
print(sorted(x,reverse=True))
print(x[::-1])

print(reversed(x)) #It reverses the elements and stores the result in another object
                   #and that object address is returned

#apply for loop and get one by one value from the reversed object
for p in reversed(x):
    print(p,end=" ")
print("\n")
for  p in reversed(sorted(x)):
    print(p,end=" ")

#Working with list addresses

x=[10,20,30,40,50]
y=[10,20,30,40,50]

print(x,id(x))
print(y,id(y))

print(x[0],type(x[0]),id(x[0]))
print(y[0],type(y[0]),id(y[0]))
