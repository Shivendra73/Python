'''Python Datetime module:
A date in Python is not a data type , but we can import a module named datetime to work with
dates.
'''
#ex:1
#Import the datetime module and display the current date and time:

import datetime

x = datetime.datetime.now() #modulename.classname.methodname
print(x)


print("\n\n\n")
#-----------------------------------------------------------------------------------------------------------------
#ex:2
'''Creating Date Objects:
To create a date, we can use the datetime() class (constructor) of the datetime module.

The datetime() class requires three parameters to create a date: year, month, day.

'''
x = datetime.datetime(2018, 5, 25) #creating object of daytime class of daytime module

print(x)

print("\n\n\n")

#ex:3
#The datetime module has many methods such as


#----------------------------------------------------------------------------------------------------------------------
#The strftime() Method:
#The datetime object has a method for formatting date objects into readable strings.

#The method is called strftime(), and takes one parameter i.e format, to specify the format of the returned string:
x = datetime.datetime.now()

print(x.year)
print(x.strftime("%U"))

print("\n\n\n")



#--------------------------------------------------------------------------------------------------------------------
'''
Directive	Description	                              Example	
%a	Weekday, short version	                              Wed	
%A	Weekday, full version	                              Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday	              3	
%d	Day of month 01-31	                              31	
%b	Month name, short version	                      Dec	
%B	Month name, full version	                      December	
%m	Month as a number 01-12	                              12	
%y	Year, short version, without century	              19	
%Y	Year, full version	                              2019	
%H	Hour 00-23	                                      17	
%I	Hour 00-12	                                      05	
%p	AM/PM	                                              PM	
%M	Minute 00-59	                                      41	
%S	Second 00-59	                                      08	
%f	Microsecond 000000-999999	                      548513	
%j	Day number of year 001-366	                      365	
%U	Week no of year,Sunday as the first day of week,00-53 52	
%W	Week no of year, Monday as the first day of week,00-53 52	
%c	Local version of date and time	                      Mon Dec 31 17:41:00 2018	
%x	Local version of date	                              12/31/18	
%X	Local version of time	                              17:41:00	 '''

#---------------------------------------------------------------------------------------------------------------------
print("\n\n\n")
#ex:1  ---->%a	Weekday, short version	                              Wed
x = datetime.datetime.now()

print(x.strftime("%a"))

#--------------------------------------------------------------------------------------------------------------
print("\n\n\n")
#ex:2 %A	    Weekday, full version	                              Wednesday	
x = datetime.datetime.now()

print(x.strftime("%A"))











