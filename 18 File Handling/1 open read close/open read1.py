
#f=open('demo1.txt',mode='r')  #reading txt file

#f=open('C:/python630am/string3.py',mode='r')   #reading a python file
#f=open('C:/python1/sample.java',mode='r')     #reading java file
f=open('F:/emp1.csv',mode='r')                #reading csv file
#f=open('F:/emp.xlsx',mode='r')                #cannot read this excel file
print(f.read())

f.close()
