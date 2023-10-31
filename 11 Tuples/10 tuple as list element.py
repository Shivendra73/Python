#Case 2: tuple as list element

x=[[10,20,30],[40,50,60],(70,80,90)]

print(x,len(x))

x[0][1]=25
x[1][2]=3.5
#x[2][0]=75
print(x)

x[2]="python"
print(x)

x[1]=True

x[0]=3.5

print(x)
