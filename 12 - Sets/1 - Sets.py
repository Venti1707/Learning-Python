a = {"Apple", "Banana", "Cherry"}

# Tuples are used to store multiple items in a singular variable
# It is the 3rd of 4 built-in data types to store collections of data
# The other 3 are: List, Tuple & Dictionary
# Tuples are unordered, unchangeable and do not allow duplicate values
# Tuples are written with curly brackets - {}
# Items in a tuple are not indexed and as such the items within can appear in a different order every time you use them
# The following values are considered to be the same, so they cannot exist simultaneously in a set
# 1 & True
# 0 & False

# To find the number of items in a set, use the len() function
print("Number of items in set a")
print(len(a))

# The items within a set can contain items that are 1 or more data types
b = {2, 3, 5}
c = {True, False, False}
d = {"Apple", True, 3}

# You can also use the set() constructor
e = set((2, "Banana", False))

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