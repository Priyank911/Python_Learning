class bank:
    tempaccount=5555
    accountlist = {}
    
    def _init_(self,amount,pin):
        self.pin=pin
        self.balance=amount
        bank.tempaccount += 1
        self.accountnumber = bank.tempaccount
        self.print_details()
        
    def print_details(self):
        print("the account number is :",self.tempaccount)
        print("the balance is :",self.balance)
        print("the pin is :",self.pin)
        
    def app(self):
        acc=int(input("\nenter your account number:"))
        p=int(input("\nenter your pin code:"))
        
        if(acc==self.accountnumber and self.pin==p):
            print("welcome\n")
            self.menu()
        else:
            print("\nyou have entered wrong credentials!")
            self.app()
            
    def menu(self):
        print("press 1 to check balance")
        print("press 2 to change pin")
        print("press 3 to transfer amount\n")
        
        i=int(input("\nenter your choice"))
        if i==1:
            print(self.balance)
            self.menu()
        elif i==2:
           self.change_pin()
           self.menu()
        elif i==3:
            acc = int(input("enter the account number:\n"))
            address = bank.accountlist[acc]
            
            amount = int(input("enter the amount"))
            self.transfer(address,amount)
    
    def change_pin(self):
        p = int(input("enter your current pin"))
        if(self.pin==p):
             q = int(input("enter your new pin"))
             self.pin=q
             print("your pin has been updated successfully")
        else:
            print("you have entered wrong pin")
            self.change_pin()
            
    def transfer(self,account,amount):
        if self.balance>=amount:
            self.balance -=amount
            account.balance = account.balance + amount
            print("success")
            print(self.balance)
            print(account.balance)
        else:
            print("you don't have sufficient amount")
            
    def add_account(self,address):
        bank.accountlist.update({self.accountnumber : address})
        print(bank.accountlist)
            
        
          
a=bank(5000,4560)
a.add_account(a)
b=bank(6000,4890)
b.add_account(b)

a.app()
