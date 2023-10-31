class sample:
    pass

s1=sample() #Rc=1
s2=sample() #Rc=2
s3=s2
print(s1)
print(s2)
print(s3)

del s1  # Rc becomes 0,Garbage collector is called, s1 is removed.
#print(s1)
del s2  #Rc becomes 1, Rc=1
del s3  #Rc becomes 0,Garbage collector is called, s3 is removed
#print(s2)
#print(s3)
