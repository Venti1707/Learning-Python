a = ["Apple", "Banana", "Cherry"]

# To add an item at the end of a list, use the append method
# The append method takes in 1 argument
# 1) value; The value of the new item
print("Adding a new element to the end of list a with the append method")
print(a)
a.append("Durian")
print(a)

# To add an item at the a specific index in a list, use the insert method
# The append method takes in 2 argument
# 1) index; The index of the new item
# 2) value; The value of the new item
print("Inserting a new element to list a with the insert method")
print(a)
a.insert(4, "Elderberry")
print(a)

# To append items from 1 list to another, use the extend method
# The extend method takes in 1 argument
# 1) iterable; Any iterable object (Tuples, sets, dictionaries)
print("Adding items from other iterables")
b = ["Fig"]
c = ("Guava", "Honeydew")
print(a)
a.extend(b)
a.extend(c)
print(a)