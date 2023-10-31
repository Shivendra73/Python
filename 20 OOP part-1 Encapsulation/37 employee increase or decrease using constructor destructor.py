
# Using Constructor incrementing employees 
# Using Destructor decrementing employees

class employee:
    
    empcount=0
    def __init__(self,x,y):
        self.ename=x
        self.salary=y
        employee.empcount+=1
    def __del__(self):
        employee.empcount-=1
    def displayemployee(self):
        print("NAME:",self.ename,"SALARY:",self.salary)
        
emp1=employee("Rohith",30000.00) #RC=1
emp2=employee("Ajith",40000.00)  #Rc=1

emp1.displayemployee()
emp2.displayemployee()
print("Total No of employees:",employee.empcount)
del emp1 #Rc becomes 0 and destructor called and emp1 is removed.
print("Total No of employees:",employee.empcount)
del emp2 #Rc becomes 0 and destructor called and emp2 is removed
print("Total No of employees:",employee.empcount)



