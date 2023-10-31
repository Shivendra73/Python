#TypeError:
#a=5#
#b='3'
#print(a+b)

try:
    a=5
    b='3'
    print(a+b)
    
except(TypeError):
    print('Unsupported operation')
    
except:
    print("Error")


