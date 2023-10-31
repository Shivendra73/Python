

#Dictionaries within a dictionary
customer={"Name":"James","bal":50000,"Bank":"HDFC","Address":{"street":"Gandhinagar","city":"Hyd","state":"Telangana"}}
print(customer)
print(customer['Name'])
print(customer['Address'])
print(customer['Address']['city'])
print(len(customer['Address']))


details={"Name":"Kohli","age":30,"wife":{"Name":"Anushka","age":28},"city":"Delhi"}
print(details)
print(details['Name'])
print(details['wife'])
print(details['wife']['Name'])
print(details)
details["wife"]['Name']="Alia"
print(details)

#Ex:3
x={"cities" : ["PUNE","MUMBAI","DELHI"]}
#Task: modify or change Mumbai to Ahmedabad

print(x)
y=x["cities"]
print(y,type(y))
y[1]="Ahmedabad"
print(y)
print(x)

#or
x["cities"][1] = "Ahmedabad"
print(x)

print("\n\n")
#changing Ahmedabad to chennai
x["cities"][1] = "chennai"
print(x)


x=10
y=x
print(x,id(x))
print(y,id(y))

x=20
print(x,id(x))
print(y,id(y))

x=10
print(x,id(x))
print(y,id(y))

y=20
print(x,id(x))
print(y,id(y))


x=[10,20,30]
y=x
z=[10,20,30]

print(x,id(x))
print(y,id(y))
print(z,id(z))

x[1]=25
print(x,id(x))
print(y,id(y))

y[2]=3.4
print(x,id(x))
print(y,id(y))

x=[70,80,90]
print(x,id(x))
print(y,id(y))

#ex:                                   
                                                     
x={"students":[{"name":"James","branch":"CSE","college":"JNTU"},
               {"name":"Arjun","branch":"ECE","college":"MGIT"},
               {"name":"Alia","branch":"IT","college":"VNR"}]} 
print(x)
print("\n")
print(x,len(x))
print(x["students"],type(x["students"]),len(x["students"]))

#accessing 1st dictionary----->1st student details
print(x["students"][0])
print(x["students"][0],type(x["students"][0]),len(x["students"][0]))
#printing the name------>"Alia"
#accessing particular key of a particular student
print(x["students"][2]["name"])

#accessing all students using for loop i.e accessing one by one dictionary
for p in x["students"]:
    print(p)



#displaying values of each key of each inner dictionary ------>  James  CSE  JNTU
for p in x["students"]:
    print(p["name"],p["branch"],p["college"])
    
for p in x["students"]:
    print("name:",p["name"])
    print("branch:",p["branch"])
    print("college:",p["college"])

#or
for p in x["students"]:
    for q in p:
        print(q,":",p[q])

print("\n")

#Modifying a dictionary value:
#changing the name Alia to sonia
x["students"][2]["name"]="sonia"
print(x)


#lists ,tuples within a dictionary

x={"emps":[(101,"miller",20000,"m",11),
           (102,"James",40000,"m",12),
           [103,"George",60000,"m",13],
           [104,"Amar",90000,"f",12]]}

#printing the value(list)
print(x["emps"],type(x["emps"]),len(x['emps']))
#printing each element of the list
for p in x["emps"]:
    print(p,type(p))

#Access name and salary of George
print(x["emps"][2][1],x["emps"][2][2])
print(x["emps"][2][1:3])

#replace the name "George" with "John"
x['emps'][2][1]="John"
print(x)

#to check whether "James is available in the list or not
for p in x["emps"]:
    if(p[1]=="James"):
        print("search successfull and the details are:",p)
#or   
for p in x["emps"]:
    if("James" in p):
        print("search successfull and the details are:",p)
























