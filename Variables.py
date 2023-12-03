#Variables---->

#<-------String---------->
#Here Variables are Container to store the Value

# first_name = "Priyank" # Here Python direct take string value without declare
# last_name = "Panchal"
# # print(type(first_name))  # By using Type you can get the datatype type..
# full_name = first_name + last_name  # Here if you want to space create a space like that ----> "  "
# full_nameSpace = first_name + "  " + last_name
# print("Hi" + full_nameSpace)

#<------Int----------->

# age = 21

# print(type(age)) // here you can check the datatype type by using ....
# age = age + 15
# print("Your age is:- ", age) # here you print integer value but you want to print value in forcefully str datatype then use typecasting
# print("Your age is print in String Datatype:- " + str(age)) # here both are different 

# Here we use Format method so we can not explicitly typecast the age variable to a string... 

# print(f"Your age is: {age}")  # method--1
# print("Your age is: {}".format(age)) # method--2

#<------Float-------->

# height = 216.15
# print(type(height)) #here also same use of type for datatype
# print("Your height is:- {}".format(height) ,"m") # here we take a best example to understand the float datatype + format method 


# The format method in Python is used for formatting strings. It allows you to create a string template with placeholders, and then replace those placeholders with actual values. Here's a simple example:
#<----code---method:-1--->

# name = "John"
# age = 25
# message = "My name is {} and I am {} years old.".format(name, age)
# print(message)

#<---Code-----method:-2---->

# message = f"My name is {name} and age is {age}"
# print(message)

#<---Boolean---->

# value = True
#print(type(value))
# print("M:-1..Are you a "+ str(value) +" Human")
# print(f"M:-2..Are you a {value} human")
# print("M:-3..Are you a {}".format(value) ,"Human")

#<---Complex--->

# Complex= 5 + 1j
#print(type(Complex)) # here also same
# print("Printing the Complex Number is:- ", Complex)
# print("Printing the complex number using format method {}".format(Complex))
# print(f"Printing the complex number using format method:-2 {Complex}")