

#try-except finally block
#FileNotFoundError:
try:
    f=None
    f=open("C:/data/demo11.txt","r")
    if(f!=None):
        print("File opened successfully")
        print(f.read())
    else:
        raise FileNotFoundError

except(FileNotFoundError):
    print("File doesnt exist")
    
except:
    print("Error")
    
finally:
    if(f!=None):
        f.close()
        print("File closed successfully")
    else:
        print("file not opened")
    
