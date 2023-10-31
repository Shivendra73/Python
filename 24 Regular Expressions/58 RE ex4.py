#finditer():Returns a Iterator object which yields Match object for every match

#To print the start and end of the match.
import re
regex="[a-zA-Z]+ \d+" 
matches=re.finditer(regex,"June 15,August 9,Dec,Jan 31,Feb 21") 
#finditer() returns iterator object
#findall() returns list object,here list doesnt support start() and end() methods
print(matches) #It prints the address
for match in matches:
     print("match start index and end index:",match.start(),match.end())

 

 
