# args = parameter that will pack all argument into a tuples useful so that a function can accept a varying amount of argument

def add(*args):
    sum= 0
    args=list(args)
    args[0]=12
    for i in args:
        sum += i
    return sum
print(add(1,2,3,4,5,6,7,8,9,10))