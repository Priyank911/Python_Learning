# **kwargs = parameter that will pack all argument into a dictionary useful so that a function can accept a varying amount of keyword argument

def hello(**kwargs):
    # print("Hello " + kwargs['first']+" "+kwargs['last'])
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value, end=" ")
hello(title="Developer",first="Priyank",last="Panchal")