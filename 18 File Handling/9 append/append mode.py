#append mode
f=open("sample.txt",mode="r+")
f.write("\n105,Ajay,80000,12,Hyd\n106,Arjun,90000,13,Pune") #if file already exists, it appends
                       #if file doesnt exist, it creates a new file
                       #if the program executed for 5 times,5 times appended
f.seek(0)
print(f.read())    
f.close()

#Here each time we are appending same record, but i want to append differt record
#in each execution
