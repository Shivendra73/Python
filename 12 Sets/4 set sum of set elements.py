
#performing sum of set elements 
x={10,20,30,40,50,10,20}

print(x,len(x))
print("sum=",sum(x))

#without sum()
sum=0
for p in x:
    sum=sum+p

print("sum=",sum)
    
#finding the sum of 3 elements out of 5 elements

sum=0
count=1
for p  in x:
    sum=sum+p
    if(count==3):
        break
    count=count+1
print("sum=",sum)










    
