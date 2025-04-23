# If multiple literals are present in your code with same variable name then how does python decides which variable to use when it is called. Here comes the LEGB concept which python follows.

# SCOPE
# L - Local function
# E - Enclosing function
# G - Global
# B - Built In variables

# E.g.

name = "This is global"

def greet():
    
    name = "This is Enclosing"
    
    def hello():
        global name             # here calling name from global scope
        # name = "This is Local"
        print("Hello " + name)
    hello()

greet()