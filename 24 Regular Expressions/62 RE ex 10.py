
#Return the domain type including .com or .in etc of given email-ids
import re
regex='@\w+[.]\w+'
result=re.findall(regex,'Techm@gmail.com, osmania@ac.in, naresh@online.com, abc@rest.biz,naresh@yahoo.co.in') 
print(result) 

