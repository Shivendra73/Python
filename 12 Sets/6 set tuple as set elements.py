
#tuples as set elemnts
x={(10,20,30),(40,50,60),(70,80,90)} #only immutable elements are allowed within set
print(x)
print(type(x))
print(len(x))

#printing each tuple
for p in x:         #printing each tuple
    print(p,type(p))

#printing each element of each tuple using nested for loop.  
for p in x:         #printing elements of each tuple
    for q in p:
        print(q,type(q))

#Note: For every value of p,inner for loop executes for 3 times---->total---->9times

#x={[10,20,30],[40,50,60],[70,80,90]}  #we cant have list as set elements
                                       #as they r mutable
#print(x)



