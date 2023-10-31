

#re module defines many functions
#RegEx Functions
''' The re module offers a set of functions that allows us to search a string for a
 match:

Function	Description
findall	        Returns a list containing all matches
finditer        Returns a iterator object
search	        Returns a Match object if there is a match anywhere in the string
sub	        Replaces one or many matches with a string 
match           for matchings  '''
#--------------------------------------------------------------------------------------------------
#findall():
#ex:1
#1)[]---->A set of characters
#ex:[a-m]

import re

str1 = "python supports Dynamic datatypes"

#Find all lower case characters  between "a" and "m" from the above string

x = re.findall("[a-m]", str1)  #returns list containing all matches
print(x)

print("\n")
#-------------------------------------------------------------------------------------------------
#ex:2
#2) \d ---->any one digit

import re

#Find all digital characters from the below string

str1 = "Kohli scored 92 runs today out of 104 balls"

#Find only the numeric values from the above string
x=re.findall("\d+",str1)
print(x,type(x))

#Extract only one digit no's

x = re.findall("\d", str1)      #for all 1 digit no's
print(x)
                
x = re.findall("\d{2}", str1)   #for all 2 digit no's
print(x)

#or
x = re.findall("\d\d", str1)   #for all 2 digit no's
print(x)
#or
x = re.findall("[0-9][0-9]", str1)   #for all 2 digit no's
print(x)
#or
x = re.findall("[0-9]{2}", str1)   #for all 2 digit no's
print(x)

x = re.findall("\d{3}", str1)     #for all 3 digits 
print(x)
print("\n")

x = re.findall("\d+", str1)      #for all digits
print(x)
print("\n")

#ex:2
str1="101.45 102 30 5 57.35"
x = re.findall("\d+", str1)
print(x)

#ex:3
str1="101.45,102,30,5,57.35"
x = re.findall("\d+", str1)
print(x)

x=re.findall("\d+[.]\d+|\d+",str1)
print(x)


#--------------------------------------------------------------------------------
#ex:3
#3)^  ------>starts with
import re

str = "hello world"

#Check if the string starts with 'hello':

x = re.findall("^hello", str)
print(x,type(x))  #returns a list
if(x):
  print("Yes, the string starts with 'hello'")
else:
  print("No match")
print("\n")
#-----------------------------------------------------------------------------------
#ex:4
#4)$ ----->ends with
import re

str = "hello world"

#Check if the string ends with 'world':

x = re.findall("world$", str)
print(x,type(x))
if (x):
  print("Yes, the string ends with 'world'")
else:
  print("No match")
print("\n")
#-------------------------------------------------------------------------------------
#ex:5
#5) * -------> 0 or more occurences of preceeding character
import re

str = "The rain in Spain falls mainly in the plain!....."

#Check if the string contains "ai" followed by 0 or more "x" characters:

x = re.findall("aix*", str)
print(x)

#----------------------------------------------------------------------------------------
#ex:6
#6)+ --------> 1 or more occurences
import re

str = "The rain in Spain falls mainly in the plain!..."

#Check if the string contains "ai" followed by 1 or more "x" characters:

x = re.findall("aix+", str)

print(x)


#Extract the words containing "ai"
x = re.findall("[a-zA-Z]+ai[a-zA-Z]+", str)
print(x)


#----------------------------------------------------------------------------------------
#ex:7
#7) {m}:Exactly the specified number of occurrences

import re

str = "The rain in Spain falls mainly in the plain!"

#Check if the string contains "a" followed by exactly two "l" characters:

x = re.findall("al{2}", str)
            
print(x)
          
#-------------------------------------------------------------------------------------------------
#8) |

str1="Python is easier than C Language"
#Check if the string contains either "Python" or "Java":

x = re.findall("Python|Java", str1)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
#--------------------------------------------------------------------------------------------------













             






  
