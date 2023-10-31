

#super(): This stmt is used to call super class method or constructor through
#sub class method or constructor

class A:
    def __init__(self):
        print("from constructor A.....")
        
class B(A):
    def __init__(self):
        super().__init__()           #Executes super class constructor
        print("from constructor B.....")


b1=B()
#here first super class constructor executes followed by sub class constructor
#here first base class logic executes and then derived class logic executes
