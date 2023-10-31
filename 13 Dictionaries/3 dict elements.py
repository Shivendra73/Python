
#dictionary is used for collection of various details(k,V)pairs about a #particular object.
#ex: customer,employee,student,etc.

customer={"name":"Ajay","AccNo":30129684561,"Branch":"Ameerpet","type":"savings"}
employee={"name":"Nikhil","sal":70000,"Desig":"manager","Branch":"Ameerpet"}
student={"name":"pranay","branch":"CSE","college":"JNTU","Loc":"kukatpally"}
print(customer)
print(employee)
print(student)
#Accessing elements of a dictionary using key------>If u pass the key, u will get the value.  
print(employee["name"])
print(student["name"])
print(student["college"])
print(employee["sal"])
#print(customer["name","AccNo"]) 
print(customer["name"],customer["AccNo"])

#ex:
x=[10,20,30,40,50]

#print(x[1,2])
print(x[1],x[2])

#printing only keys using for loop
for p in employee:
    print(p)
    
#printing only values using for loop

for p in employee:
    print(employee[p])

#printing both keys and values using for loop

for p in employee:
    print(p,":",employee[p])

















