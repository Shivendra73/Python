#Method oveloading :

class A:
    def add(self,x,*y):
        if(x=='int'):
            result=0  #initial result =0
        if(x=='str'):
            result=' ' #initial result =null
        for p in y:
            result=result+p
        print(result)
    '''def add(self,a):
        print(a) '''
a1=A()
a1.add('int',10,20,30) #performs addition
a1.add('str','web','technology') #performs concatenation
#a1.add(10)

#Here there is no method overloading or polymorphism ,bcoz here
# no multiple methods ,here only one method is performing multiple tasks
#but in method overloading, we define multiple methods.
