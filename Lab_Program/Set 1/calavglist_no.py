number = int(input("Enter Length of list: "))
arr = list(map(int,input().split()))[:number]
sum = 0
for i in arr:
    sum = sum + i 
avg = sum / number
print("Average of list is: ", avg)