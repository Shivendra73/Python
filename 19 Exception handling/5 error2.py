#AttributeError

#x=(10,20,30,40,50)
#x.append(60) #AttributeError
#x[1]=25  #TypeError


try:
    x=(10,20,30,40,50)
    x.append(60)
    x[1]=25
    
except(AttributeError):
    print("Tuple doesnt support Insertion")
    
except(TypeError):
    print("Tuple elements cannot be modified")
    
except:
    print("Error Occured!!!")   


