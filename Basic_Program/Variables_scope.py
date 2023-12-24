# Scope = The region that a variables is recognized
#         A variables is only availables from inside the region it is created.
#         A global and locally scoped versions of a variables can be created 

name = "Developer" # global scope (availables inside & outside function)

def display_name():
    name="Priyank" # local scope (available only inside this function)
    print(name)

display_name()
print(name)

# Priority in types of Variables:- 
# 1. Local Variables
# 2. Enclosing variables
# 3. global variables
# 4. built in