def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n-1
    return num
n = int(input("Enter the number: "))
fac = factorial(n)
print(fac)