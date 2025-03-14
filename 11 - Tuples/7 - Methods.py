# There are 2 methods for tuples in Python, these are

# 1) tuple.count(value)
# Returns the number of times a specified value occurs in a tuple
# value - The item to search for
a = ("Apple", "Banana", "Cherry", "Banana", "Durian")
b = "Banana"
print("Counting how many times " + b + " appears in tuple a")
print(a.count(b))

# 2) tuple.index(value)
# Searches the tuple for a specified value and returns the position of where it was first found
# Raises an exception if the value is not found
# value - The item to search for
print("Finding the index of the first instance of " + b + " in tuple a")
print(a.index(b))
# c = "Elderberry"
# print("Finding the index of the first instance of " + c + " in tuple a")
# print(a.index(c))