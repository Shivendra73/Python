'''testdata.txt ------>present in C:\data  folder
101,Miller,10000,11,Hyd
102,Blake,20000,12,Pune
103,Sony,30000,11,hyd
104,Sita,40000,12,pune
105,John,50000,13,hyd'''

f=open("C:/data/testdata.txt")
x=f.readlines()
print(x)

print("\n\n")

#reading only emp names and salaries
for p in x:
    print(p.split(",")[1],p.split(",")[2])
    #print(p.split(",")[1:3])






   
    
