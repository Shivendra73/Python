

#to print month and date in a seperate lines
import re
regex="([a-zA-Z]+) (\d+)"
x=re.sub(regex,r"\2 of \1","June 15,August 9,Dec 12,Jan 31")#x stores o/p of sub----->15 of June,...
print(x)
regex1="\d+ [a-zA-Z]+ [a-zA-Z]+" # RE for--->15 of June
matches=re.findall(regex1,x)
for match in matches:
    print(match)

print("\n\n")
#If i want only month then keep the pattern in bracket
regex="([a-zA-Z]+) (\d+)"
x=re.sub(regex,r"\2 of \1","June 15,August 9,Dec 12,Jan 31")#x stores o/p of sub----->15 of June,...
regex1="\d+ [a-zA-Z]+ ([a-zA-Z]+)" # RE for--->15 of June
matches=re.findall(regex1,x)
for match in matches:
    print(match)


