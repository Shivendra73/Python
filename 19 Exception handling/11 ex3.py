
#ValueError
try:
    marks=int(input('Enter the marks:'))
    if(marks > 100):
        raise ValueError

except(ValueError):
    print(marks, "is out of allowed range")

else:
    print("MARKS:",marks)
