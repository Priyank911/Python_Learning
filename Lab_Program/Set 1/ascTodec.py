# size_list = int(input("Enter the number: "))
# arr = list(map(int,input().split(" ")))[:size_list]
# order = sorted(arr)
# print(f"{order} is ascending")
# print(f"{order[::-1]} is descending")

size_list = int(input("Enter the number: "))
arr = list(map(int,input().split(" ")))[:size_list]
arr.sort()
print(f"{arr} is ascending")
print(f"{arr[::-1]} is descending")