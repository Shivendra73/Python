
#To capture DOB---->month and day
import re
regex="[a-zA-Z]+ \d+" 
x=re.findall(regex,"June 15th,August 9,Dec 12,Feb 22,jul ,hello ,chennai") #jul is invalid
print(x)
for match in x:
     print(match)
print("\n")


#II) #To capture  only month
regex="([a-zA-Z]+) \d+" #it extracts only the pattern within parenthesis
x=re.findall(regex,"June 15th hyd,August 9,Dec 12,Feb 22,jul ,hello,chennai") #jul is invalid
print(x)
for match in x:
     print("month:",match)
print("\n")
      
#III) #To capture  only date but not month
regex="[a-zA-Z]+ (\d+)" #it extracts only the pattern within parenthesis
x=re.findall(regex,"June 15th,August 9,Dec 12,Feb 22,jul ,2020,2019") #jul is invalid
print(x)
for match in x:
     print("Date:",match)
print("\n")

#ex:3
data='''Miller DOB: June 15th,
Blake DOB: August 9th
Ajay DOB: Febrauary 21st
Amar DOB: march 17th'''


#Extract only  month and day


x=re.findall("[a-zA-Z]+ \d+",data)
print(x)
#or
regex1="[a-zA-Z]+ \d+" 
x=re.findall(regex1,data) 
print(x)
print("\n")



#ex:4
#extract only emp names now
data='''Miller DOB: June 15th,
Blake DOB: August 9th
Ajay DOB: Febrauary 21st
Amar DOB: march 17th'''


x=re.findall("([a-zA-Z]+) [a-zA-Z]+",data)
print(x)
#or
x=re.findall("([a-zA-Z]+) [A-Z]+",data) 
print(x)
#or
y=re.findall("(\w+) [A-Z]+",data) 
print(y)
#or
x=re.findall("([a-zA-Z]+) [D]",data)
print(x)
#or
x=re.findall("([a-zA-Z]+) DOB",data) 
print(x)
#or
x=re.findall("(.+) DOB",data) 
print(x)#
#ex:5
#extract only names and months

data='''Miller DOB: June 15th,
Blake DOB: August 9th,
Ajay DOB: Febrauary 21st,
Amar DOB: march 17th'''

x=re.findall("[a-zA-Z]+ ",data) 
print(x)
#or
regex2="(\w+) "
y=re.findall(regex2,data)
print(y)
#or
x=re.findall("([a-zA-Z]+) [A-Z:]+ ([a-zA-Z]+)",data) 
print(x)
#or
x=re.findall("([a-zA-Z]+) DOB: ([a-zA-Z]+)",data) 
print(x)

#Extract only Miller and June

x=re.findall("Miller |June",data) 
print(x)


#extract only---> DOB

x=re.findall("([A-Z]+):",data) 
print(x)
#---------------------------------------------------------------------------------------------
#zip():for merging 2 lists

subs=["maths","phy","chem"]

marks=[90,80,70]

x=zip(subs,marks)
print(x,type(x))

y=list(x)
print(y,type(y))

z=dict(y)
print(z,type(z))
#---------------------------------------------------------------------------------------------
#ex:6
#Create a dictionary from the above data by extracting name as key and month as value
#first create 2 lists-->names and months and merge those lists and convert to dictionary
#using zip() function

#extract only emp names as one list

data='''Miller DOB: June 15th,
Blake DOB: August 9th,
Ajay DOB: Febrauary 21st,
Amar DOB: march 17th'''

#Extract names
regex2="([a-zA-z]+) DOB"
enames=re.findall(regex2,data)
print(enames)

#extract only months
regex2=": ([a-zA-z]+)"
months=re.findall(regex2,data)
print(months)

#Merging 2 lists using zip() function
x=zip(enames,months)
print(x,type(x))

y=list(x)
print(y,type(y))

z=dict(y)
print(z,type(z))




