#Different ways of creating a list: 2ways

#1.using [ ]
#2.using list() function

#Creating list using list() function

x=list() #Empty list is created
print(x)
print(len(x))

#Ex:2 Creating a list with content
y=list("python")
print(y)
print(len(y))

#Ex:3
'''
y=list("python","Java") #Error--->bcoz list() function accepts only one argument
print(y)                #and that argument should be iterable type like string,list,tuple,set
print(len(y))
'''
'''
#ex:4
y=list(10)   #Error--->bcoz int is not iterable
print(y)
print(len(y))
'''
#ex:4
y=list([10,20,30,40,50])
print(y)
print(len(y))

#ex:5
y=list((10,20,30,40,50))
print(y)
print(len(y))






















