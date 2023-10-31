#String Functions

x="hello"

#1.len(): returns no of characters within the string
print(len(x))

#2.max(): returns the max valued character
print(max(x))

#3.min():
print(min(x))

#ex:2
y="Hello"
print(min(y))

#ex:3
z="virat kohli"
print(min(z))

#ex:4
date="dec7"
print(min(date))

#ASCII Values
'''
A-65
B-66
C-67
.
.
Z-90

a-97
b-98
.
.
.
z-122
'''
#String Special characters
#1. + :Concatenation :Adding 2 strings ----->1st string followed by 2nd string

x="Hello world"
#Extract "Hello" and add "India"
print(x[0:5]+" "+"India")

#2.*: Repeatition

x="hello"
print((x+" ")*3)
print(3*x)

#3.in or not in

x="python"

print('p' in x)
print('a' not in x)
print('a' in x)





























