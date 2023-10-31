
#working with dictionary addresses

x={"a":10,"b":20}
print(x,id(x))

y={"a":10,"b":20}
print(y,id(y))

print(x is y) #address
print(x == y) #content

print(x["a"],type(x["a"]),id(x["a"]))
print(y["a"],type(y["a"]),id(y["a"]))

print(x["a"] is y["a"])

p=10

print(p is x["a"])
print(p == x["a"])

a=[10,20,30]
print(a[0] is x["a"])


