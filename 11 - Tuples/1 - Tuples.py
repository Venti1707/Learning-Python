a = ("Apple", "Banana", "Cherry")

# Tuples are used to store multiple items in a singular variable
# It is the second of 4 built-in data types to store collections of data
# The other 3 are: List, Set & Dictionary
# Tuples are ordered, unchangeable and allow duplicate values
# Tuples are written with round brackets - ()
# Items in a tuple are indexed (like in a list)

# To find the number of items in a tuple, use the len() function
print("Number of items in tuple a")
print(len(a))

# In order to create a tuple with only a single item, after the first item, a comma has to be added
print("A tuple with only a singular item")
b = ("Apple") # This is not a tuple
print(type(b))
c = ("Apple",) # This is a tuple
print(type(c))

# The items within a list can contain items that are 1 or more data types
d = (2, 3, 5)
e = (True, False, False)
f = ("Apple", True, 3)

# The tuple() constructor can also be used to make a tuple
print("Using the tuple() constructor to make a tuple")
g = tuple(("Apple", "Banana", "Cherry"))
print(g)
print(type(g))

""""
| ---------- | -------- | ------------------ |--------------------------|
| Type       | Ordered? | Changeable?        | Allows duplicate members?|
| ---------- | -------- | ------------------ |--------------------------|
| List       | Yes      | Yes                | Yes                      |
| Tuple      | Yes      | Yes                | Yes                      |
| Set        | No       | No*, and unindexed | No                       |
| Dictionary | Yes**    | Yes                | No                       |

*Set items are unchangeable, but you can remove and/or add items whenever you like
**As of Python version 3.7, dictionaries are ordered; In Python 3.6 and earlier, dictionaries are unordered
"""