lis = []
n = int(input("Enter the number:- "))
tp = ()
check = set()
count = 0
for i in range(n):
    s = input()
    lis.append(s)
for word in lis:
    tp = tuple(sorted(word))
    check.add(tp)
print(len(check))