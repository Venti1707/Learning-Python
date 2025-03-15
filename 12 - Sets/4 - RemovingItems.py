a = {"Apple", "Banana", "Cherry", "Durian", "Elderberry", "Fig", "Grapes"}

# To remove items in a set you can either use the remove() or discard() method
# The remove() method raises an error if the item does not exist
# The discard() method will not raise an error if the item does not exist
print("Removing items from set a with the remove() method")
print(a)
# a.remove("Honeydew") # If a is printed after this line, an error will be raised
a.remove("Grapes")
print(a)

print("Removing items from set a with the discard() method")
print(a)
a.discard("Honeydew")
a.discard("Fig")
print(a)

# The pop() method can also be used but is not recommended as it removes a random item
# The item to be removed is random due to sets being unordered
print("Removing items from set a with the pop() method")
print(a)
a.pop()
print(a)

# Deleting the entire set is done with the del keyword
# del a # If a is printed, this will produce an error as set a no longer exists