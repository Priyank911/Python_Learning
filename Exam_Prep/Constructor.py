class Atm:
    def __init__(self): # Constructor 
       # print("Hello")
      self.pin = ""
      self.balance= 0

      # Here we what we do call menu method inside the class
      self.menu()

    def menu(self):    # Here we decalre method name as menu
       user_input = input("""
        Hello, How you would like to proceed?
            1. Enter 1 to create pin
            2. Enter 2 to deposite
            3. Enter 3 to withdraw balance
            4. Enter 4 to check to balance
            5. Enter 5 to exit
""")
       if user_input == "1":
          self.create_pin()
       elif user_input == "2":
          self.deposite()
       elif user_input == "3":
          self.withdraw()
       elif user_input == "4":
          self.check_balance()
       else:
          print("Thank You")

    def create_pin(self):
       self.pin = input("Enter the Pin:- ")
       print("Pin Set Successfully")

    def deposit(self):
       check = input("Enter the Pin:- ")
       if check == self.pin:
          amount = int(input("Enter the Amount:- "))
          self.balance = self.balance + amount
          print("Deposite Successful")
       else:
          print("Invalid Pin ")
    
    def withdraw(self):
       check = input("Enter the Pin:- ")
       if check == self.pin:
          amount = int(input("Enter the Amount:- "))
          if amount< self.balance:
             self.balance = self.balance - amount
             print("Withdraw Successfully")
          else:
             print("Insufficent Balance")
       else:
          print("Invalid Pin")
    
    def check_balance(self):
       check = input("Enter the Pin:- ")
       if check == self.pin:
          print(self.balance)
       else:
          print("Invalid Pin")

call = Atm()
call.deposit()
call.withdraw()
call.check_balance()
