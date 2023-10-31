

#Calendar module in Python has the calendar class that allows the calculations for
#various task based on date, month, and year.

#1.Create a plain text calendar

import calendar
c = calendar.TextCalendar(calendar.SUNDAY)#creating a text calendar ,Start of the month will be Sunday.
str1 = c.formatmonth(2022, 1) #creating calendar for the year 2021 for the month July
print(str1)



#ex:2 #start of month as Monday
c = calendar.TextCalendar(calendar.MONDAY)
str2 = c.formatmonth(2022, 1)
print(str2)
print(type(str2))


#ex:3
# Create an HTML format calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
str1 = hc.formatmonth(2022, 1)
print(str1)


#ex:4
c = calendar.TextCalendar(calendar.SUNDAY)
for i in c.itermonthdays(2022,1):
    print(i)
#Zeros in the output mean that the day of the week does not belong to that month.



#ex:5  Printing monthnames from the calender
for p in calendar.month_name:
    print(p)
    
print("\n") 
x=list(calendar.month_name)
print(x)

#Printing a particular month
print(x[6])

print("\n")
#ex:6  Printing daynames from the calender
for p in calendar.day_name:
    print(p)

print("\n") 
days=list(calendar.day_name)
print(days)

#Printing a particular day
print(days[4])
