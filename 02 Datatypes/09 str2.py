#String Slicing: Extracting particular portion of a string
x="python program"
print(x)
#Extract---->"python"
print(x[0:6])# Always upper bound is excluded
#Extract---->"prog"
print(x[7:11])
print(x[11:7]) #Empty String bcoz always slicing in the forward direction.

#Extract---->"prog" using -ve index
print(x[-7:-3])

#Extract---->"program"
print(x[7:14])
print(x[7: ])
print(x[-7: ])

print(x[ :6])
print(x[ : ])
print(x[:])
print(x)
print(x[0: ])
print(x[-7:11])
print(x[0:14:2])
print(x[::2])
print(x[::-1])#It reverses the string











