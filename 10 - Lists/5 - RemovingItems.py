a = ["Apple", "Banana", "Banana", "Cherry", "Durian", "Elderberry", "Fig"]

# To remove specific items, use the remove() method
# If there are duplicate items within a list, the remove() method only removes the first occurrence
print("Removing items with the remove() method")
print(a)
a.remove("Banana")
print(a)

# To remove items based off their index values, either use the pop() method or the del keyword
# If no index is stated for the pop() method, it will delete the last item
# If no index is started for the del keyword, it will delete the entire list
print("Removing items from list a with the pop() method")
print(a)
a.pop(4)
print(a)
a.pop()
print(a)

print("Removing items from list a with the del keyword")
print(a)
del a[3]
print(a)
# del a # This will be produce an error if printed as the list no longer exists

# To clear the list, use the clear() method
print("Clearing list a with the clear() method")
print(a)
a.clear()
print(a)