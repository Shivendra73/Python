
#sub() :for substitutions 
#To print date and month
import re
regex="([a-zA-Z]+) (\d+)" #extracts month and also date bcoz both r in parenthesis 
print(re.sub(regex,r"\2 of \1","June 15,August 9,Dec 22,Jan 31,Feb 21"))
#\2 of \1, means 15 of June,means 2nd pattern extracted first and then extracts 1st pattern
#To print each in separate line 

#help(re)
