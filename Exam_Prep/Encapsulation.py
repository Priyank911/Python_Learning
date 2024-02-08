class Atm:
    def __init__(self):
        self.__pin = ""
        self.__balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
        Hello, How would you like to proceed?
            1. Enter 1 to create pin
            2. Enter 2 to deposit
            3. Enter 3 to withdraw balance
            4. Enter 4 to check balance
            5. Enter 5 to exit
""")
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("Thank You")

    def create_pin(self):
        self.__pin = input("Enter the Pin: ")
        print("Pin Set Successfully")

    def deposit(self):
        check = input("Enter the Pin: ")
        if check == self.__pin:
            amount = int(input("Enter the Amount: "))
            self.__balance = self.__balance + amount
            print("Deposit Successful")
        else:
            print("Invalid Pin")

    def withdraw(self):
        check = input("Enter the Pin: ")
        if check == self.__pin:
            amount = int(input("Enter the Amount: "))
            if amount < self.__balance:
                self.__balance = self.__balance - amount
                print("Withdraw Successfully")
            else:
                print("Insufficient Balance")
        else:
            print("Invalid Pin")

    def check_balance(self):
        check = input("Enter the Pin: ")
        if check == self.__pin:
            print(self.__balance)
        else:
            print("Invalid Pin")

    # Getter method for __pin
    def get_pin(self):
        return self.__pin

    # Setter method for __pin
    def set_pin(self, new_pin):
        self.__pin = new_pin
        print("Pin are Changed")

    # Getter method for __balance
    def get_balance(self):
        return self.__balance

    # Setter method for __balance
    def set_balance(self, new_balance):
        self.__balance = new_balance


call = Atm()
call.set_pin("0911")  # Example of using setter for pin
print(call.get_pin())   # Example of using getter for pin


""" 
Here What Happen when we declare __pin so python
convert internaly his name into "_Atm__pin"

Note:- In python Nothing is Truly private

"""