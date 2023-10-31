import mod1
y=20

z=mod1.x+y

def show():
    mod1.display()
    print("y=",y)
    print("z=",z)
show()

print(dir())#It displays the properties of current module(main module) along with built-in attributes
print(dir(mod1))

#print(),len(),id(),type(),sum(),max(),min(),sorted() etc all are the built-in functions present
#in one module called __builtins__

#__builtins__ is the only module in python without importing,we can use its properties.
print(dir(__builtins__))

