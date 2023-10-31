

#with stmt:
#The with statement can be used while opening a file, The Advantage of with stmt is
#It takes care of closing a file which is opened by it.
#with stmt follows space indentation
data='''
1.Python is Simple
2.python is user-friendly
3.Pyhon supports interactive mode
4.Python supports 89300 modules
5.Python has many built-in libraries
6.Python supports object-oriented programming
7.Python supports all major databases
8.Python is dynamic typed
9.python provides simple syntaxes
10.Python is extensible ''' 

with open("sample.txt",mode="w") as f:
    f.write(data) 

with open("sample.txt",mode="r") as f1:
    print(f1.read())   

      #(or) reading using for loop
with open("sample.txt",mode="r") as f2:
    for line in f2:
        print(line)
