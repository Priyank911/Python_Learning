number = int(input("Enter the number: "))
print(f"The Table of {number} -- ")
for i in range(1,11):
    temp = number * i
    print(f"{number} * {i} = {temp}")
