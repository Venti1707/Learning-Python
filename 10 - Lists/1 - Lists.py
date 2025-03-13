a = ["Apple", "Banana", "Cherry"]

# Lists are used to store multiple items in a singular variable
# It is the first of 4 built-in data types to store collections of data
# The other 3 are: Tuple, Set & Dictionary

# Lists are ordered which means that the items have a defined order, and that order will not change
# When new items are added to the list, they will be placed at the end of the list
# There are methods that will change the order of the list but in general the order will not change

# Lists are changeable which means that we can change, add or remove items after it is created

# Lists can contain duplicate values due to each item within being indexed

# To find the length of a list, use the len() function
print("Length of list a")
print(len(a))

# The items within a list can contain items that are 1 or more data types
b = [2, 3, 5]
c = [True, False, False]
d = ["Apple", True, 3]

# You can also use the list() constructor
e = list((2, "Banana", False))

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