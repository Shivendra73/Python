

#try-except else block: if no exception in try block then ctrl goes to else block

#FileNotFoundError:
try:
    f=open("C:/data/demo5.txt","r")   #r--->read mode
    print(f.read())
    f.close()

except(FileNotFoundError):
    print("File doesnt exist")
    
except:
    print("Error")

else:
    print("File opened Successully")
print("end")


