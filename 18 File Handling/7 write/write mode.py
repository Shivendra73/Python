

#creating a file and writing data into it.

f=open("sample1.txt",mode="w")  #This file object f is created only for writing data
#f=open("C:\python1030amm\demo1.txt",mode="w")

data=''' 1.Python is Simple
2.python is user-friendly
3.Python supports interactive mode
4.Python supports 89300 modules
5.Python has many built-in libraries
6.Python supports object-oriented programming
7.Python supports all major databases
8.Python is dynamic typed
9.python provides simple syntaxes
10.Python is extensible '''

f.write(data)
f.write("\nhello Ajay...how r u??\n") #if file already exists,it truncates(removes) the data
                                      #and writes the new data
f.write("Hi...")            #if file doesnt exist, it creates a new file and writes
f.close()  #if we wont close, we can not write into it  or delete it
  # If we close the file then only we can see the data

f1=open("sample1.txt","r")   #here f1 is only for reading
#f1=open("C:\python1030amm\demo1.txt","r")
print(f1.read())    
f1.close()

