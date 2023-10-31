#Logical operators :These Operators gives Logical relationship b/w 2 objects

#Logical operators also returns either True/False

#Varous Logical operators are
#1.and
#2.or
#not
'''
     x       y       x and y    x or y
     True    True    True        True
     True    False   False       True
     False   True    False       True
     False   False   False       False

Logical and returns True only if both the conditions are True else it returns False
Logical or returns True if both the conditions are True or if any one condition is True
Logical or returns Flase only if both the conditions are False'''

x=10
y=20
z=30

p=(x>y) and (z>x)
print(p)

q=(x>y) and (z>x) or (y!=z)
print(q)

r=(x>y) and (z==x+y) or (y==z-x)
   
print(r)

print(not True)
print(not False)





