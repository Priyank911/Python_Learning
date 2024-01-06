class Account:

  sampleAcc = 12345

  def __init__(self,name,amount,pin):
    Account.sampleAcc += 1
    self.accountNumber = Account.sampleAcc
    self.name = name
    self.balance = amount
    self.pin = pin
    self.printDetail()

  def printDetail(self):
    print(self.name)
    print(self.accountNumber)
    print(self.balance)
    print(self.pin)
    print()

class Staff:
  id = 0


  def __init__(self,name,pin):
    Staff.id += 1
    self.id = Staff.id
    self.name = name
    self.pin = pin
    self.printDetail()


  def printDetail(self):
    print(self.id)

    print(self.pin)
    print()

class Bank:

  # to start customer app create object of Bank class and call userApp().
  # to start Staff app call staffApp() with the help of the object

  accountList = {}
  staffList = {}

  def __init__(self):
    self.login = 0
    self.staffLogin =0

  def createAccount(self,name,amount,pin):
    acc = Account(name,amount,pin)
    Bank.accountList.update({acc.accountNumber : acc})

  def userApp(self):
    self.accLogin()

  def accLogin(self):
    acc = int(input('enter your account number'))
    pin = int(input('enter your pin number'))

    if acc in Bank.accountList:
      if pin == Bank.accountList[acc].pin:

        print('welcome')
        self.login = acc
        self.menu()

      else:
        print('you have entered wrong details')

  def menu(self):
    print('press 1 to check your balance')
    print('press 2 to change your pin')
    print('press 3 to transfer amount')
    print('press 4 to exit')
    i = int(input())

    if i==1:
      a = Bank.accountList[self.login].balance
      print(a)
      self.menu()


    elif i==2:
      self.changePin()
      self.menu()

    elif i ==3:
      acc = int(input('enter account number'))
      amount = int(input('enter your amount'))
      self.transfer(self.login,acc,amount)
      self.menu()

    elif i==4:
      pass

  def changePin(self):
    i = int(input('enter your current pin'))
    if Bank.accountList[self.login].pin == i:
      pin = int(input('enter your new pin'))
      Bank.accountList[self.login].pin = pin
      print('your pin has been changed successfully')
    else:
      print('you have entered a wrong pin')

  def transfer(self,account1,account,amount):
    if account1 in Bank.accountList and account in Bank.accountList:
      if  Bank.accountList[account1].balance >= amount:
        Bank.accountList[account1].balance -= amount
        Bank.accountList[account].balance += amount
        print(f'your amount transfered successfull your balance is : {Bank.accountList[account1].balance}')
      else:
        print('you have low balance')
    else:
      print('you have entered wrong account')

  def deposit(self,account,amount):

      Bank.accountList[account].balance += amount
      print(f'yout amount deposit successfull your balance is : {Bank.accountList[account].balance}')


  def withdrawal(self,account,amount):

    if  Bank.accountList[account].balance >= amount:
      Bank.accountList[account].balance -= amount

      print(f'your amount withdrawal is successfull your balance is : {Bank.accountList[account].balance}')
    else:
      print('you have low balance')

  def createStaff(self,name,pin):
    a = Staff(name,pin)
    Bank.staffList.update({a.id: a})


  def staffApp(self):
   self.sLogin()


  def sLogin(self):
    acc = int(input('enter your id number'))

    if acc in Bank.staffList:
      pin = int(input('enter your pin number'))
      if pin == Bank.staffList[acc].pin:

        print('welcome')
        self.staffLogin = acc
        self.menu2()
    else:
        print('you have entered wrong details')
        self.staffApp()

  def menu2(self):
    print('press 1 to create account')
    print('press 2 to transfer amount')
    print('press 3 to deposite')
    print('press 4 to withdrawal')
    print('press 5 to exit')
    i = int(input())

    if i==1:
      name = input('enter your name')
      amt = int(input('enter your amount'))
      pin = int(input('enter your pin number'))
      self.createAccount(name,amt,pin)

      self.menu2()


    elif i==2:
      acc1 = int(input('enter first account number'))
      acc2 = int(input('enter second account number'))
      amount = int(input('enter your amount'))
      self.transfer(acc1,acc2,amount)
      self.menu2()

    elif i ==3:
      acc = int(input('enter account number'))
      amount = int(input('enter your amount'))
      self.deposit(acc,amount)
      self.menu2()

    elif i==4:
      acc = int(input('enter account number'))
      amount = int(input('enter your amount'))
      self.withdrawal(acc,amount)
      self.menu2()

    elif i == 5:
      pass

bank = Bank()
bank.createStaff('xyz',1234)

bank.staffApp()

bank.userApp()

a = Bank.accountList[12347].balance
print(a)