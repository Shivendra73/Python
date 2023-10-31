
#mathematical operations using set methods
A={10,20,30,40,50}
B={10,20,60,70,80}
print(A)
print(B)

print(A|B)
print(B|A)
print(A.union(B))
print(B.union(A))

print(A & B)
print(B & A)
print(A.intersection(B))      #Common elements
print(B.intersection(A))

print(A-B)            #Removing elements of B from set A 
print(B-A)
print(A.difference(B))
print(B.difference(A)) 

print(A^B)#common elements are removed
print(B^A)
print(A.symmetric_difference(B))
print(B.symmetric_difference(A))



A={"Ajay","Blake","Rohith","Miller","James"}
B={"James","Pavan","Raj","George","Ajay"}

#I want those who are in both the sets
print(A.intersection(B))

#I want those names which are not part of B
print(A.difference(B))










