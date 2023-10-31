

#creating a .csv file and writing into it.
f=open("emp.csv",mode="w")
f.write("101,Miller,75000,m,11") #file already exists, so it truncates
f.write("\n102,Blake,85000,m,12")
f.write("\n103,John,95000,m,13")
       #if file doesnt exist, it creates a new file and writes
f.close()

f1=open("emp.csv")
print(f1.read())    
f1.close()



