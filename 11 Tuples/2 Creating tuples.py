#Creating tuples

x=(10,20,30,40,50)               #Homogeneous tuple
print(x)
print(type(x)) 
print(id(x))
print(len(x)) 

y=(101,"Blake",70890.70,"pune")    #Heterogeneous tuple
print(y)
print(type(y))
print(len(y))


z=10,20,30
print(z)
print(type(z))
print(len(z))

cities="hyd","pune","mumbai","chennai"
print(cities,type(cities),len(cities))


w=("python")#If there is only one element within a tuple then it is not a tuple.
print(w,type(w),len(w))

p=("python",)
print(p,type(p),len(p))

q=(10)
print(q,type(q))

r=(10,)
print(r,type(r),len(r))

s1=10
print(s1,type(s1))

s2=10,
print(s2,type(s2),len(s2))

x=([10,20,30])
print(x,type(x),len(x))

x=([10,20,30],[40,50])
print(x,type(x),len(x))

y=({10,20,30})
print(y,type(y),len(y))


x=[10]
print(x,type(x))
#-------------------------------------------------------------------------------------------

#Creating a tuple using tuple():
x=tuple()   #Empty tuple created
print(x)
print(type(x))
print(len(x))

#Creating a tuple with content
x=tuple("mumbai")
print(x)
print(type(x))
print(len(x))

''''
#Ex:2
x=tuple("mumbai","chennai") #Error ----->Bcoz tuple() accepts only one argument and
print(x)     #that argument should be of iterable type like  string,list,tuple,set
print(type(x))
print(len(x)) 
'''

#Ex:3
'''
x=tuple(10)          #Error---->bcoz int is not iterable
print(x)
print(type(x))
print(len(x))'''

#ex:4
x=tuple(["mumbai","chennai"])
print(x)
print(type(x))
print(len(x))

#Note:If we pass a string to a tuple() function--->then each character of string will be taken
#     as element of the tuple.
#     IF we pass any collection to a tuple() function--->each element of the collection
#     will be considered as the element of the tuple.

#ex:5
x=tuple((10,20,30))
print(x)
print(type(x))
print(len(x))

#ex:6
x=tuple({10,20,30,40})
print(x)
print(type(x))
print(len(x))































