import random
import string
a = int(input("Enter the number of Pasword for Generate:- "))
def passgen(a):
  password = " " 
  t = string.ascii_letters + string.digits + string.punctuation
  for i in range(a):
   password += random.choice(t)
  print(password)
passgen(a)