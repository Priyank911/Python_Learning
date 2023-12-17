# Nested Loops = The "inner loop" will finish all of it's iteration before finishing one  iteration of the "outer loop"

rows = int(input("How many rows: "))
columns = int(input("How many columns: "))
symbol = input("Enter the symbol to print: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()