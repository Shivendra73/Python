#List slicing: Extracting particular elements

x=[10,20,30,40,50,60]

print(x)
#Extract---->10,20,30
print(x[0:3]) #Always upper bound is excluded
#Extract--->30,40,50
print(x[2:5])
print(x[5:2]) #Empty list--->bcoz always slicing in the forward direction
#Extract---->30,40,50 using -ve index
print(x[-4:-1])
#Extract---->30 to 60
print(x[2:6])
y=x[2:6]
print(y,type(y))
print(x[2: ])
print(x[-4: ])
print(x[ :3])
print(x[ : ])
print(x)
print(x[0: ])
print(x[-4:4])

print(x[0:6:2])
print(x[::2])
print(x[::-1]) #prints the list in the reverse orde

#Extract those elements which are divisible by 3
x=[10,20,30,40,50,60]

for p in x:
    if(p%3==0):
        print(p)








