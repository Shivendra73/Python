
import re
regex="([a-zA-Z]+) (\w+)"
x=re.sub(regex,r"\2 is capital of \1","Telangana Hyderabad,Ap Amaravathi,Karnataka Bengluru,maharashtra Mumbai")#x stores o/p of sub----->15 of June,...
print(x)
