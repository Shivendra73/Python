
#Reading specific lines---->3rd and 5th line

file1=input("Enter the file path:")

with open(file1) as f1:
    for line in(f1.readlines()[2:5:2]):
        print(line,end="")


