
#Tuples wthin a tuple

x=(("Kohli",95),("Dhoni",45),("Rohith",82),("Hardik",30))
print(x,len(x))

for p in x:
    print(p,type(p))

for p,q in x:
    print("PLAYER:",p)
    print("RUNS:",q)

#--------------------------------------------------------------------------------------------
#ex:2
emps=((101,"Miller",50000,"Manager"),
      (102,"Blake",60000,"Professor"),
      (103,"James",70000,"Teacher"),
      (104,"Ajay",80000,"Principal"))

print(emps,len(emps))

for p in emps:
    print(p,type(p))

for p,q,r,s in emps:
    print("EID:",p)
    print("ENAME:",q)
    print("SALARY:",r)
    print("DESIGNATION:",s)
    print("=======================")












    
