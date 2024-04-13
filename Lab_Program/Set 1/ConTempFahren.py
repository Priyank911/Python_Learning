print("Temperature Convertor Fahrenheit to Celsius and Vice Versa")
print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")
choice = int(input("Enter the choice: "))
if choice == 1:
    celsius = float(input("Enter the Value of Celsius: "))
    fahrenheit = (celsius * 1.8) + 32
    print("Answer: ",fahrenheit)
if choice == 2:
    fahrenheit = float(input("Enter the Value of Fahrenheit: "))
    celsius = (fahrenheit-32) * 5/9
    print(celsius)