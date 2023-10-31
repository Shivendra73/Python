#overriding __str__() method


class x:
    
    def __str__(self):  #overriding __str__() method of object class
        return "hello...." #so it returns hello.... instead of address
    def m1(self):
        print("from m1.....")
x1=x()

print(x1)
print(x1.__str__())


x2=x()
print(x2)
print(x2.__str__())
x1.m1()



#here all the objects displaying or returning  same value,
#but i want each object to display different value
