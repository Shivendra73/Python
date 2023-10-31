import re

#Check if the string starts with "python" and ends with "java":

txt = "python is easier and simpler than Java"
x = re.search("^python.*Java$", txt)#. indicates any character,* indicates multiple occurences
#print(x)
if (x):
  print("Matching")
else:
  print("No match")

  

  





