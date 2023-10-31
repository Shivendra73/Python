

class x:
    def m1(self):
        print("from m1....")

x1=x()
print(x1) #returns indirect address in hexadecimal value
print(x1.__str__()) #it also returns indirect address in hexadecimal value
print(x1.__hash__()) #it returns indirect address in decimal format.

