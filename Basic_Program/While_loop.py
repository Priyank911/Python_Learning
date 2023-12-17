#While Loop = a statement that will execute it's block of code, as long as it's condition remain true...

# Name= input("Enter your name:- ")

# while len(Name) == 0:
#     Name = input("Enter the name:- ")

# print("Hello"+Name)

# Method:-2

Name = None
while not Name:
    Name = input("Enter Your name: ")
print("Hello "+ Name)