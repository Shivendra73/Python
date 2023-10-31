import re
regex="([a-zA-Z]+) (\w+) (\d+)"
x=re.sub(regex,r"\2 capital of \1 has covid cases of \3","Telangana Hyderabad 15000,Ap Amaravathi 25000,Karnataka Bengluru 30000,maharashtra Mumbai 40000")#x stores o/p of sub----->15 of June,...
print(x)
print("\n")



#ex:2
x=re.sub(regex,r"\1 has covid cases of \3","Telangana Hyderabad 15000,Ap Amaravathi 25000,Karnataka Bengluru 30000,maharashtra Mumbai 40000")#x stores o/p of sub----->15 of June,...
print(x)

