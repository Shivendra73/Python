
class customer:
    '''CUSTOMER APPLICATION'''
    
    def getdetails(self):
        self.custname=input("Enter customer name:")
        self.accno=int(input("Enter Account NO:"))
        self.address=input("Enter Address:")
        self.balance=int(input("Enter balance:"))
    def putdetails(self):
        print("Customer Name:",self.custname)
        print("Account No:",self.accno)
        print("Address:",self.address)
        print("Balance:",self.balance)
    def deposit(self):
        self.damount=int(input("Enter deposit Amount:"))
        self.totalamount=self.balance+self.damount
        print("totalamount:",self.totalamount)
    def withdraw(self):
        self.wamount=int(input("Enter withdraw amount:"))
        self.totalamount=self.totalamount-self.wamount
        print("Totalamount after withdraw:",self.totalamount)
c1=customer()
c1.getdetails()
c1.putdetails()
c1.deposit()
print("totalamount:",c1.totalamount) 
c1.withdraw()
print("Name:",c1.custname)
print("totalamount:",c1.totalamount)


        
