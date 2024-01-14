# args = parameter that will pack all argument into a tuples useful so that a function can accept a varying amount of argument

def add(*args):
    sum= 0
    # args=list(args)  # here we do Updation in args using list 
    # args[0]=12     # By passing a Value in List using indexing
    for i in args:
        sum += i
    return sum
print(add(1,2,3,4,5,6,7,8,9,10))