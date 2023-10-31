#Nested Lists: Lists within a list:

x=[[10,20,30],[40,50,60],[70,80,90]]

print(x,len(x))

#printing each sub-list
print(x[0],type(x[0]),id(x[0]),len(x[0]))
print(x[1],type(x[1]),id(x[1]),len(x[1]))
print(x[2],type(x[2]),id(x[2]),len(x[2]))
print("\n")
#printing each sub-list using for loop.

for p in x:
    print(p,type(p),id(p),len(p))

#printing each element of each sub-list
for p in x:
    for q in p:
        print(q,type(q),id(q))

print(x[0][0])
print(x[1][2])
print(x[2][0])

#printing only the 1st element from each list
for p in x:
    for q in p:
        print(q,type(q),id(q))
        break
print("\n")
#printing only the 1st 2 elements from each list
for p in x:
    count=0
    for q in p:
        print(q,type(q),id(q))
        count=count+1
        if(count==2):
            break









