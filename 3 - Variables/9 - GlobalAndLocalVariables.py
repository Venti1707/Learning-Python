# Global variables are created outside functions.
# They can be used inside & outside functions.
a = "Global"

def function1():
    print(a)

function1()

# If a variable is declared within a function, it's known as a local variable
def function2():
    a = "Local"
    print(a)

function2()

# To create a global function within a function, the global keyword can be used
def function3():
    global c
    c = "Global within a function"
    print(c)

function3()