#Nested lists: Lists within a list

emps=[["JAmes",90000],["Miller",80000],["Ajay",70000]]

for p in emps:
    print(p,type(p))

for p,q in emps:
    print("NAME:",p)
    print("SALARY:",q)
