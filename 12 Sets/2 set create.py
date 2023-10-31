
#creating set object
x={10,20,30,40,50}  #homogeneous elements

print(x)
print(type(x))
print(len(x))

y={501,6.1,True,"hello"} #heterogeneous elements
print(y)
print(type(y))
print(len(y))

z={10,20,30,(30,40,50,60)}  # only immutable elements are allowed within the set
print(z)
print(type(z))
print(len(z))


#creating a set using set function
a=set()         #creating empty set
print(a)        
print(type(a))  
print(len(a))

#ex:2
b=set("hello")    #creating set with data
print(b)          #only one parameter allowed witin a set() 
print(type(b))    #i.e iterable types like string,list,tuple,set etc
print(len(b))

#ex:3
'''
b=set("hello","hai")   
print(b)         
print(type(b))    
print(len(b))'''

#ex:4
'''
b=set(10)  
print(b)         
print(type(b))    
print(len(b)) '''


b=set(["hello","hai"])   #Note:If u pass any collection to set() then the length of
#the collection will be the length of set ignoring the duplicates
print(b)         
print(type(b))    
print(len(b)) 

m=set([10,20,30,40,10])    
print(m)          
print(type(m))  
print(len(m))


m=set((10,20,30,40,10))    
print(m)          
print(type(m))  
print(len(m))

n=set({10,20,30,40})    
print(n)          
print(type(n))  
print(len(n))
#--------------------------------------------------------------------------------
#diff b/w---->set((1,2,3,4)) 
#Note: Using curly  braces,whatever elements are present are taken as it is
#      but whenever we use set() function and if we pass any collection to it, only the
#      elements will be taken

a={(1,2,3,4,5)}
print(a)
print(len(a))

b=set((1,2,3,4,5))
print(b)
print(len(b))

c=set([(1,2,3),(4,5,6)]) 
print(c)
print(len(c))

'''
d=set(([1,2,3],[4,5,6])) 
print(d)
print(len(d))
'''
#----------------------------------------------------------------------------------

c={10,20,10,20,30} #duplicate elements will be eliminated
print(c)
print(len(c))

'''d={{10,20,30},{40,50,60},{70,80,90}} # sets within set are not allowed
print(d)'''












