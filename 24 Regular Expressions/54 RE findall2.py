#Examples

import re

#ex1: Extract only years from the following data
#Extract only year and construct a list from it.

data='''
1st worldcup held in the year 1975
2nd worldcup held in the year 1979
3rd worldcup held in the year 1983
4th worldcup held in the year 1987
5th worldcup held in the year 1992
6th worldcup held in the year 1996
7th worldcup held in the year 1999'''

x=re.findall("\d\d\d\d",data)
print(x)
#or
x=re.findall("\d{4}",data)
print(x)
#or
x=re.findall("[0-9][0-9][0-9][0-9]",data)
print(x)
#or
x=re.findall("[0-9]{4}",data)
print(x)

#Ex:2 I want all 1 digit,2 digit, 3 digit ,4digit no's (only numericals) from the above string

x=re.findall("\d+",data)
print(x)





#Ex:3 A pattern which can extract numericals and alphabets
str="a,A,_,9,$,%"







x=re.findall("\w",str)
print(x)

#Ex:4 A pattern which can extract only special symbols
x=re.findall("\W",str)
print(x)

#ex:5 only special symbols excluding comma

x=re.findall("[^A-Za-z0-9_,]",str)
print(x)
 
#ex:6 A pattern wwhich can extract all these

str1="oct2,Jan26,Aug15,Jan_1,August,2019"
x=re.findall("\w+",str1)
print(x)

 
#ex:7 A pattern wwhich can extract all these
str1="oct2,Jan26,Aug15,Jan_1,August,2019,45000$,$720"

x=re.findall("\w+",str1)
print(x)

#ex:8 A pattern which can extract only special symbols
str1="oct2,Jan26,Aug15,Jan_1,August,2019,45000$,$720"
x=re.findall("\W",str1)
print(x)

#ex:9 A pattern which can extract only $ excluding comma
str1="oct2,Jan26,Aug15,Jan_1,August,2019,45000$,$720"
x=re.findall("[$]",str1)
print(x)

#ex:10 A pattern which can extract $ along with the numericals attached to it

str1="oct2,Jan26,Aug15,Jan_1,August,2019,45000$,$720"

x=re.findall("\d*[$]\d*",str1)  #or re.findall("\d+[$]|[$]\d+",str1)
print(x)

#ex:11 A pattern which can extract any number,lowercase,uppercase,special characters
str1="7,a,A,bb,_,$,+,*,++,hyderabad,me@gmail.com"
x=re.findall(".+",str1)
print(x)

#ex:12 
#Extract only height values from the following data and compute the max height value

data=''' Blake=6.3,
Miller=5.8,
James=5.11,
John=5
Amar=6.5'''


x=re.findall("\d[.]\d+|\d+",data)
print(x)
y=[]
for p in x:
    y.append(float(p))
print(y)
print("max height=",max(y))

#ex:13
#Extract only weight values from the following data
data=''' Blake=82.57,
Miller=78.25,
James=105.90,
John=89
Amar=97.30'''


x=re.findall("\d+[.]\d+|\d+",data)
print(x)

#ex:14
#Extract only scores from the following data and compute the total score
scorecard='''Rohith=45
Kohli=104
Dhoni=34
Raina=44
Dhawn=38
Ghambir=8
'''
x=re.findall("\d+",scorecard)
print(x)

scores=[]

for p in x:
    scores.append(int(p))
print(scores)
print("Total Score=",sum(scores))



































