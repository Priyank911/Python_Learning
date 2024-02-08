class Customer:
    def __init__(self,name): # here we declare method
        self.name = name
def greet(customer): # here we declare function
    customer.name = "Nitish"
    print(customer.name)
    # if customer.gender == "Male":
    #     print("Hello",customer.name,"Sir")
    # else:
    #     print("Hello",customer.name,"Ma'am")

Call = Customer("Priyank")

greet(Call)
print(Call.name)

"""

Here we learn that here we pass object of class
as a parameter to the function

"""

