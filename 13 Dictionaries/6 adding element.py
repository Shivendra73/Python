


#modifying,adding and printing an element of a dictionary
std={"name":"kumar","height":5.6,"weight":75}
print(std)
print(len(std))
print(std["name"])  #value of the key will be printed

#modifying the weight
std["weight"]=80          #if key availabe it modifies else creates a new key
print("after modifying \n",std)

#adding new elements into dictionary.
std["age"]=28           #insertion order is not followed
std["city"]="Chennai"
print("after adding:\n",std)



