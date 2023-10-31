#List methods:
x=[10,20,30,40,50]
print(x,len(x))

#1.append(): For appending an element at the end of the list
x.append(60)
print(x,len(x))

#x.append(70,80) #error--->bcoz append() accepts only one argument

#appending multiple elements using append() and for loop
for p in (35,45,55):
    x.append(p)
print(x,len(x))
#--------------------------------------------------------------------------------------------
#2.extend(): for extending a list with the elements of other list
y=[1.5,2.5,3.5,4.5,5.5]
x.extend(y)
print(x,len(x))
#--------------------------------------------------------------------------------------------
#3.insert(index,value):for inserting an element at the desired position
x.insert(2,25)
print(x)

x.insert(4,"pune")
print(x,len(x))
#----------------------------------------------------------------------------------------------
#4.pop(index): For removing an element based on index
x.pop(5)
print(x)

#remove the element 55

#5.index(element): returns index of an element
print(x.index(55))
x.pop(9)
#---------------------------------------------------------------------------------------------
#6.remove(value): removes an element based on value
x.remove(30)
x.remove("pune")
print(x)
#-------------------------------------------------------------------------------------------
y=[10,20,30,40,50,10,20,30,10,20,30]
y.remove(20) #It removes only the 1st occured 20
print(y)

#Task:remove the 2nd ocurred 10
print(y.index(10,2))
y.pop(4)
print(y)

#--------------------------------------------------------------------------------------------
#ex:2
emps=[[101,"Miller",30000,"hyd"],[102,"Blake",40000,"pune"],[103,"James",50000,"hyd"]]

#Task: remove the city field from every record
#emps.pop()
#print(emps)
for p in emps:
    p.pop(3)
print(emps)

#removing a list using using particular id
for p in emps:
    if(p[0]==103):
        emps.remove(p)
print(emps)
'''
for p in emps:
    p.pop(3)
print(emps)
'''    
#---------------------------------------------------------------------------------------------
#ex:3
emps=[[101,"Miller",30000,"hyd"],[102,"Blake",40000,"pune"],[103,"James",50000,"hyd"]]

#Task: Extract only names and sort them in order

names=[]

for p in emps:
    names.append(p[1])
print(names)
print(sorted(names))

#---------------------------------------------------------------------------------------------
#7.count(): to count the no of occurences of an element in a list
medals=["IND","AUS","ENG","IND","AUS","ENG","IND","JAPAN","AUS"]
print(medals.count("IND"))

#---------------------------------------------------------------------------------------------
#8.sort():
emps=["Rohith","Ajay","Miller","Blake","James"]
emps.sort()
print(emps)

#---------------------------------------------------------------------------------------------
#9.copy(): For duplicating a list
x=[10,20,30,40,50]
y=x.copy()
print(y)

































