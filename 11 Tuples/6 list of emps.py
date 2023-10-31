
#Accepting list of emps

emps=[]
n=int(input("Enter the no of employees to be added:"))
for p in range(1,n+1):
    x=input("Enter the Name of emp"+str(p)+":")
    emps.append(x)
print(emps)
