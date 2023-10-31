

#Program to read last 'n' lines from a file
file1=input("Enter the file path:")
n=int(input("Enter the value of n:")) #n--->last 'n' lines

with open(file1) as f1:
    print("Last",n,"lines are:")
    for line in(f1.readlines()[-n:]):
        print(line)


