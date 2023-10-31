


import re
regex="[a-zA-Z]+ \d+" #, regex is a variable
#+ indicates one or more occurance of a character, follwed by
#one space,followed by 1 or more occurance of a digit.
x=re.findall(regex,"June 15,August 9,Dec12,May ,oct ,Feb 2020,2021")
#findall is a fn for searching a given pattern in given string
#it takes 2 parameters---> regex and string 
#x is a list of matched strings
print(x)
for match in x:
     print("Full match:",match)






#Note:if------> regex="[a-zA-Z]+ \d*"----->then May ,oct also will be extracted
