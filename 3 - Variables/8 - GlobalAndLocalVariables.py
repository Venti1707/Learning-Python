# Global variables are created outside functions
# They can be used inside & outside functions
a = "Global variable outside a function"

def function1():
    print(a)

function1()

# If a variable is declared within a function, it is known as a local variable
def function2():
    a = "Local variable within a function"
    print(a)

function2()

# To create a global function within a function, the global keyword is used
def function3():
    global c
    c = "Global variable within a function"
    print(c)

function3()