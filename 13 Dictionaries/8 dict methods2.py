
#methods of a dictionary

x={"name":"amar","branch":"CSE","Rank":5}
print(x)
print(id(x))
print(x["name"])
print(x.get("name"))
x.pop("branch") #removing particular key
print(x)
x.popitem()    #randomly any key will b removed
print(x)
print(x.clear())
print(type(x),len(x),id(x))

x["name"]="James"
print(x,id(x))

