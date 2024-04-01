"""
A decorator is a design pattern in Python that allows you to add extra functionality to an existing function or method,
without modifying its source code. Decorators are implemented using Python's function or class syntax, and they take the 
function or class as a parameter, and return a new function or class with the additional behavior.
Decorators are commonly used for things like logging, caching, and access control. They help to make your code more modular, reusable, and easier to maintain.
"""
def demo(func):
    def inner(a):
        print("******")
        func(a)
        print("******")
    return inner
@demo
def x(a):
    print(a)
y = x("Hello")