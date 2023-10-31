
#we can also raise the pre-defined exceptions explicitly by using raise keyword.
#whether a person is eligible to vote or not.
try:  
    age = int(input("Enter the age:"))  
    if(age<18):  
        raise ValueError
    else:  
        print("Eligible to Vote")
        
except ValueError:  
    print("The age is less, not eligible to vote")  
