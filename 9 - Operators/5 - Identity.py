# These operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location
a = ["Apple", "Banana", "Cherry"]
b = ["Apple", "Banana", "Cherry"]
c = a

# 1) variableName is value
# Returns True if both variables are the same object
print("variableName is value")
print(a is b) # Returns False because a is not the same object as b, even if they have the same content
print(a is c) # Returns True because a is the same object as c
print(a == b) # Returns True as the == operator does not take into account whether it's the same object

# 1) variableName is value
# Returns True if both variables are the same object
print("variableName is value")
print(a is not b) # Returns True because a is not the same object as b, even if they have the same content
print(a is not c) # Returns False because a is the same object as c
print(a != b) # Returns False as the != operator does not take into account whether it's the same object