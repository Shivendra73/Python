
#Functions applied on a tuple
x=(30,10,40,20,50)
print(x)
print(type(x))
print(id(x))
print(len(x))
print(sum(x))
print(max(x))
print(min(x))
print(sorted(x)) #Sorted() always returns  list type
print(sorted(x,reverse=True))
print(x[::-1])
print(sorted(x[::-1]))
print(sorted(x[::-1],reverse=True))

print(reversed(x)) #It reverses the elements and stores the result in another
                   #object and that object address is returned.

#Getting one by one value from the reversed object using for loop

for p in reversed(x):
    print(p,end=" ")
print("\n")

for p in reversed(sorted(x)):
    print(p,end=" ")

print("\n")

x=("Lion","Tiger","Fox","Elephant","rat")
print(max(x))
print(min(x))
print(sorted(x))

#ASCII values
'''
A-65
B-66
.
.
z-90

a-97
b-98
.
.
z-122
'''
















