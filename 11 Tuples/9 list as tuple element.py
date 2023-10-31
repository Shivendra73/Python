#Case 1: List as Tuple element

x=((10,20,30),(40,50,60),[70,80,90])

print(x,len(x))

#x[0][1]=25   
x[2][0]=75
print(x)

x[2]="python"

