import random
import string

def passgen(a):
  
  password = ""
  
  t = string.ascii_letters + string.digits + string.punctuation
  
  for i in range(a):
   password += random.choice(t)
  
  print(password)
  
passgen(10)  
