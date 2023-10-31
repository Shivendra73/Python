
class A:
    def m1(self):
        print("from m1.....")
class B(A):
    def m2(self):
        print("from m2.....")
b1=B()
print(b1)#prints hashcode value(address) stord by ref variable b1 in hexadecimal
print(b1.__hash__())# hashcode in decimal
print(hash(b1))     #hashcode in decimal
print(b1.__hash__)   #hashcode value in hexadecimal


x=10
print(x)  #here it wont print address
print(id(x))
#in above example,before creating object for class B, 2 other objects are
#created i.e class A object and Object class object, all these 3 objects
#are stored in same memory location, i.e all the original addresses of the
#3objects is taken by python interpreter and creates
#indirect address(hashcode value) based on original
#address of the objects by calling __hash__()method.
#This __hash__method converts the hashcode value in the form of
#hexadecimal format and gives that value to reference variable.
#__hash__method is present inside object class,bcoz of that reason
#object class is made as super class for every class in python.

#in above example b1 stores indirct address,but not original address,
#In python, we always work with indirect addresses,but not original
#addresses
