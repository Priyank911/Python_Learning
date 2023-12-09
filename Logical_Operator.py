# Logical Operator are :- AND/OR/NOT.
temp = int(input("What is the temperature Outside?:- "))
if not(temp >= 0 and temp <= 30):
    print("The temperature is good today..!")
    print("go Outside!")
elif not(temp < 0 or temp > 30):
    print("The temperature is bad today..!")
    print("Stay inside")