

# creating dictionary elements
x={"sachin":90,"Ganguly":65,"Dravid":35}#homogeneous keys(string type),homogeneous values(int type)
print(x)
print(type(x))
print(len(x))


emp={"eid":101 ,"ename":"James" ,"sal":90870.40,  1:"male"} #heterogeneous keys and heterogeneous values
print(emp)
print(type(emp))
print(len(emp))
print(emp["ename"])  #IF we pass the key,we get the value

print(emp[1])

z={"ECE":90,"CSE":120,"IT":60,"EEE":60,"CSE":60} #duplicate keys are not allowed,but values are allowed.
print(z)
print(type(z))
print(len(z))


x={"a":20,"b":5,"a":10,"b":15,"a":3}
print(x,len(x))
print(x['a'])  #if we pass the key----->we get the value
print(x['b'])


p={"x":100,"y":200,"y":400,"x":300}
print(p,len(p))


details={"name":"Ajay","age":25,"height":6.2}

print(details)
print(type(details),len(details))

#Accessing the values of a dictionary 
print(details["name"])
print(details["age"])
print(details["height"])

details={"name":"Ajay","age":25,"height":6.2}


for p in details:
    print(p,type(p))

#printing only values using for loop
for p in details:
    print(details[p])

#Printing both key and values:

for p in details:
    print(p,":",details[p])
    

print(details["age"],type(details["age"]))
    
#another way of creating a dictionary using dict()
a={ }   
print(a)
print(type(a))
print(len(a))

a={10,20}
print(a,type(a))

y={"a":10,"b":20}
print(y,type(y),len(y))

#Creating a dictionary using dict()
b=dict() #empty dictionary
print(b)
print(type(b))
print(len(b))

print("\n")
d={"rank":15}
print(d,id(d),len(d))


c=dict(d) #what parameters we can pass in dict function-->passing dictionary only as a parameter
print(c,type(c),len(c),id(c))
#or

e=d  #assigning one dictionary address to another dictionary.
print(e,type(e),id(e),len(e))
print(d,type(d),id(d),len(d))

x=int("10")
print(x,type(x))

'''
y=int("hello")  
print(y) '''

'''
p=dict([10,20,30,40,50])
print(p,type(p)) '''

#Creating a dictionary from a list
p=dict([("kohli",30),("Dhoni",36),("Rohith",32)])
print(p,type(p))

p=dict([["kohli",30],["Dhoni",36],["Rohith",32]])
print(p,type(p))

p=dict((["kohli",30],["Dhoni",36],["Rohith",32]))
print(p,type(p))

p=dict([{"kohli",30},{"Dhoni",36},{"Rohith",32}]) #valid but not recommended
print(p,type(p))

#In a dictionary, value can be of any type like int,float,string,bool,list,tuple,
#set,dictionary

x={"emps":["John","Miller","Rahul","Ajay"],"eid":[101,102,103,104]}
print(x,len(x))
print(x["emps"])    #If u pass the key , u will get the value as list
print(type(x["emps"]))

print(x["eid"])

#accessing the name------>"Rahul" and his id

print(x["emps"][2])
print(x["eid"][2])

#Extracting "miller" and "Rahul"
print(x["emps"][1:3])

#Printing key and values-------->names and their eid's
i=0
for p in x["emps"]:
    print(p,":",x["eid"][i])
    i=i+1

#or
i=0
for p in x["emps"]:
    print(x["emps"][i],":",x["eid"][i])
    i=i+1













