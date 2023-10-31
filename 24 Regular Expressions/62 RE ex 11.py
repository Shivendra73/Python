
#re.match():
#Validate a phone number: phone number must be of 10 digits and starts with 7 or 8 or 9
import re
x=['9983764321','7384963897','5376412769','938476182']
for val in x:
    if(re.match('[7-9]{1}[0-9]{9}',val) and len(val) == 10):
        print('Valid')
    else:
        print('Invalid')


