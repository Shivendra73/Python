

#converting list to tuple and tuple to set

#x=[10,20,30,40,50,10,20,30]
x=[[10,20,30],40,50,10,20,30]
print(x,len(x))

y=tuple(x)
print(y,type(y),len(y))

z=set(y) #duplicates eliminated,insertion order not preserved
print(z,type(z),len(z))





