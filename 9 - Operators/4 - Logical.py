# These operators are used to combine conditional statements
# They return Boolean values
a = 1707

# 1) condition1 and condition2
# Returns True when condition1 is True and condition2 is True
# condition1: 0 | condition2: 0 | returns: False
# condition1: 0 | condition2: 1 | returns: False
# condition1: 1 | condition2: 0 | returns: False
# condition1: 1 | condition2: 1 | returns: True
print("condition1 and condition2")
print((a < 1708) and (a > 22))

# 2) condition1 or condition2
# Returns True when either condition1 is True or condition2 is True
# condition1: 0 | condition2: 0 | returns: False
# condition1: 0 | condition2: 1 | returns: True
# condition1: 1 | condition2: 0 | returns: True
# condition1: 1 | condition2: 1 | returns: True
print("condition1 or condition2")
print((a < 1708) or (a > 22))

# 3) condition1 not condition2
# Returns True when False and vice versa
print("not(condition)")
print(not((a < 1708) and (a > 22)))