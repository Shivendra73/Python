import re
regex="[a-zA-Z]+ \d+"  
matches=re.findall(regex,"June 15,July 15,August 9,Dec 12,12 Feb") #12 Feb is invalid
print(matches)
for match in matches:
     print("Full match",match)
