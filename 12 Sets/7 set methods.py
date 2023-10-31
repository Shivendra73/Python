
# methods of set -----add(),copy(),update(),pop(),discard(),remove(),clear()
x={10,20,30,40,50}
print(x,id(x))

x.add(60)     #adding 60 to set
print(x,id(x),len(x))

#x.add(70,80) #error bcoz---> add() accepts only one argument

x.add((70,80,90)) # accepted but (70,80,90) taken as tuple
print("after adding:")
print(x,len(x))

#using add() and using for loop, we can add multiple elements one by one

#ex:adding 3 elements 55,65,75
for p in (55,65,75):
    x.add(p)
print(x,len(x))
#-----------------------------------------------------------------------------------------------------

#update( ): For inserting multiple elements at  a time
x.update((60,70,80)) #here 3 elements gets added
print(x,id(x),len(x))

#copy( ): for duplicating a set
y=x.copy()  #creates a copy of x
print("another copy :") 
print(y,id(y))
print(x is y)

z=x
print(z,type(z),id(z))
print(x is z)

#pop() : removes a element randomly

x.pop()     
print(x)

x.pop()     
print(x)

x.pop()     
print(x)

x.discard(20)
print(x)

x.remove(30) #removes particular element of our choice
print(x)


'''x.remove(95) #it gives error
print(x) '''

x.discard(95) #wont give any error
print(x)

x.clear()  #clears all the set elements
print(x)
print(len(x),id(x))
print(y,id(y))
print("z=",z)














