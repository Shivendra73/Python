#String methods:
#1.upper(): To print a string in uppercase

x="hyderabad"
print(x.upper())


#2.lower(): To print a string lowercase
x="MUMBAI"
print(x.lower())

#3.Capitalize(): Capitalizes the 1st character of a string
x="india"
print(x.capitalize())

#4.title(): For capitalizing the 1st character of each word in a string
x="good evening hyderabad"
print(x.title())

emps="ajay rohith james miller blake amar"
print(emps.title())

#5.swapcase(): Converts one case to another case
x="good evening hyderabad"
print(x.swapcase())

#6.replace(): For replacing a portion of a string
x="Java is Easy and Java is simple"
print(x.replace("Java","Python"))
print(x)

#ex:2
y="sachin is a good batsmen"
print(y.replace("sachin","Kohli"))

#7.count(): To count the no of occurences of each sub-string or a character.
x="hello hello hello .... how r u??"
print(x.count("hello"))
print(x.count("h"))

data='''1. Python is Simple
2. Python is user-friendly
3. Python supports interactive mode
4. Python supports 89300 modules
5. Python has many built-in libraries
6. Python supports object-oriented programming
7. Python supports all major databases
8. Python is dynamic typed
9. Python provides simple syntaxes
10.Python is extensible'''
print(data.count("Python"))

#8.strip():for removing the blankspaces before and after the string

x="       Hello Hyderabad             "
print(x,len(x))
y=x.strip()
print(y,len(y))

#9.find(): To check whether a sub-string is available or not
#If found  it returns the 1st character index position of the sub-string else it returns -1

x="Python is easier than Java"

print(x.find("Java"))
print(x.find("Hadoop"))

#10.Split(): If we split a string,we get a list
x="Good Evening Hyderabad"
y=x.split(" ")
print(y,type(y))
print(y[2])

#ex:
emp="101,Ajay,70000,Manager"
y=emp.split(",")
print(y,type(y))
print(y[1],y[3])

#11.format(): for substitutions

x="{} is the captain of Indian Team"
print(x.format("Kohli"))

y="His Name is {} and he is a {}"
print(y.format("Rohan","doctor"))
print(y.format("Dhoni","Cricketer"))

#ex:3
z="{} is the {} of {}"
print(z.format("Delhi","capital","India"))
print(z.format("Kohli","captain","Indian Team"))
print(z.format("Modi","PM","India"))

#ex:4
x="{},{},{} are the trending technologies"
print(x.format("Datascience","Python","Hadoop"))

#12.startswith()
#   endswith()

x="Python is easier than Java"
print(x.startswith("Python"))
print(x.endswith("Java"))

#13. isalpha(): It returns True if all the characters within the string are alphabets

city="hyderabad"
print(city.isalpha())

date="Dec6"
print(date.isalpha())

name="virat kohli"
print(name.isalpha())

#14. isdecimal(): It returns True if all the characters within the string are numeric


date="6 12 2021"
print(date.isdecimal())

pi="3.14"
print(len(pi))
print(pi.isdecimal())

accno="309876040"
print(accno.isdecimal())

#15. isalnum():it returns True  if all the characters within the string are either alphabets
#               or numeric or  combination of both.

date="6 12 2021"
print(date.isalnum())

pi="3.14"
print(len(pi))
print(pi.isalnum())

accno="309876040"
print(accno.isalnum())

x="Dec6"
print(x.isalnum())

pan="ALGPM2938P"
print(pan.isalnum())

#16.join(): It joins the strings of a collection

date=["6","12","2021"]
y="/".join(date)
print(y)

z="-".join(date)
print(z)


#17:parition: It returns a tuple consisting of 3 strings--->i)Before match
#                                                           ii)match
#                                                          iii)After match

cities="PUNE MUMBAI CHENNAI"
print(cities.partition("MUMBAI"))

#o/p:
#('PUNE ', 'MUMBAI', ' CHENNAI')

#ex:2

cities="PUNE CHENNAI MUMBAI"
print(cities.partition("MUMBAI"))

#o/p:
#('PUNE CHENNAI ', 'MUMBAI', '')
# BeforeMatch      Match     AfterMAtch

#ex:3
cities="MUMBAI PUNE CHENNAI"
print(cities.partition("MUMBAI"))

#o/p:
#('',         'MUMBAI', ' PUNE CHENNAI')
# BeforeMatch   Match     AfterMAtch

#ex:4
cities="MUMBAI PUNE CHENNAI"
print(cities.partition("DELHI"))

#o/p:
#('MUMBAI PUNE CHENNAI', '', '')

#ex:5
cities="MUMBAI MUMBAI MUMBAI"
print(cities.partition("MUMBAI"))

#o/p:
('', 'MUMBAI', ' MUMBAI MUMBAI')

#ex:6
cities="mumbai MUMBAI MUMBAI"
print(cities.partition("MUMBAI"))

























































































