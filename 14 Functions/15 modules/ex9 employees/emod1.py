#Renaming a module: If the modulename is too big then we can rename the module
#                   using alias name
'''
import employees as e

print(e.emp1["name"],e.emp1["sal"],e.emp1["desig"])
print(e.emp2["name"],e.emp2["sal"],e.emp2["desig"])
print(e.emp3["name"],e.emp3["sal"],e.emp3["desig"])

'''
from employees import emp1,emp2,emp3
#or
from employees import *

print(emp1["name"],emp1["sal"],emp1["desig"])
print(emp2["name"],emp2["sal"],emp2["desig"])
print(emp3["name"],emp3["sal"],emp3["desig"])
