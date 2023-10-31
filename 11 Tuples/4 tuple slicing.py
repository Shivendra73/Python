#Tuple slicing:

x=("Amar","Rohith","Rahul","Blake","James","Miller")

#Extract----"Blake" using -ve index
print(x[-3])
print(x[3])
#Extract---->first 3 names
print(x[0:3])#Always upper bound is excluded
#Extract---->"Rahul","Blake","James"
print(x[2:5])
print(x[5:2]) #Empty tuple

#Extract---->"Rahul","Blake","James" using -ve index
print(x[-4:-1])

#Extract--->"Rahul" to "miller"
print(x[2: ])
print(x[2:6])
print(x[ :3])

print(x[ : ])
print(x)
print(x[0: ])
print(x[0:6:2])
print(x[::2])
print(x[::-1]) #reverses the elements of a tuple

















