a = 22
b = 7
# Python supports 6 conditional statements
# These have been gone over in 3 - Comparison.py within the 09 - Operators folder

# When using if statements, code after the if has to be indented
# This has been gone over in 1 - Indentation.py within the 01 - Syntax folder

# The elif keyword is short for else if and is Python's way of saying "If the previous conditions were not true, then try this condition"
# The else keyword evaluates anything which is not caught by the previous conditions
print("Combining if, elif and else for checking the relationship between a and b")
if (a == b):
    print("a is equal to b")
elif (a < b):
    print("a is lesser than b")
else:
    print("a is greater than b")

# Ternary operators (or conditional expressions) are single line if else statements
# You can simplify an if statement by doing the following
# if (Condition): (Code to run)
print("Using a single line to check the relationship between a and b with if")
if (a > b): print("a is greater than b")

# You can also simply an if else statement by doing the following
# (Code to run if true) if (Condition) else (Code to run if false)
print("Using a single line to check the relationship between a and b with if and else")
print("a is greater than b") if (a > b) else print("a is smaller than b")

# You can have multiple conditions in a single ternary operator by doing the following
# (Code to run if true) if (Condition) else (Another if else statement)
print("Using a single line to check the relationship between a and b with multiple if and else")
print("a is equal to b") if (a == b) else print("a is greater than b") if (a > b) else print("a is smaller than b")

# The and keyword is a logical operator which returns true if both conditions are true
# This has been gone over in 4 - Logical.py with the 09 - Operators folder

# The or keyword is a logical operator which returns true if one of the conditions is true
# This has been gone over in 4 - Logical.py with the 09 - Operators folder

# The not keyword is a logical operator which inverses the result of the conditional statements
# This has been gone over in 4 - Logical.py with the 09 - Operators folder

# You can nest have multiple if statements inside a single if statement, which is known as a nested if
print("Using nested if statements to find the range of the c which has the value of a + b")
c = a + b
if (c > 10):
    print("c is greater than 10")
    if (c < 20):
        print("c is below 20")
    else:
        print("c is above 20")

# The pass keyword is used if an if statement has to return an empty result
print("Using the pass statement to return nothing in an if statement")
if (a > b):
    pass
else:
    print("a is smaller than a")