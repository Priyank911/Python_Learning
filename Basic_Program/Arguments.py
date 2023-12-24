# Arguments = Arguments preceded by an identifier when we pass them to a function the order of the arguments doesn't matter,
#              unlike positional arguments python know the names of the arguments that our function receives

def hello(first,middle,last):
    print("Hi.."+first+" "+middle+" "+last)

# hello("Priyank","Kumar","Panchal")
#hello("Panchal","kumar","Priyank")
hello(last="Panchal",middle="kumar",first="Priyank")