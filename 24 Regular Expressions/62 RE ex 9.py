

#Return the domain type of given email-ids
import re
regex='@(\w+)[.]\w+'
result=re.findall(regex,'mahendra@gmail.com, osmania@ac.in, techm@online.com, abc@rest.biz,rajesh@yahoo.co.in')

print(result)








