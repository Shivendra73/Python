

x=[10,2.5,True,10,"python"] #list
print(x)     #Rc=1

#Remove  float and int object

del x[1]     #RC of float object becomes 0,so  float object removed.
print(x)
del x[0]     #RC was 2,becomes 1,
print(x)
del x[1]     #RC was 1,becomes 0,int object removed.
print(x)

del x
#print(x)



