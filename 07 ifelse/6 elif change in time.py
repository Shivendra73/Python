#elif :For providing multiple conditions

#Program illustrating change in time

time=float(input("Enter the current time:"))

if(time<=12.00):
    print("Good Morning!!!")
elif(time<=16.00):
    print("Good Afternoon!!!")
elif(time<=20.00):
    print("Good Evening!!!")
else:
    print("Good Night!!!")

