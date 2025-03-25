a = {
    "name": "Nic",
    "age": 21,
    "username": "Venti1707",
    "isLearningPython": True,
    "age": 22, # This will overwrite the previous age value
    "favouriteWeapons": [
        "Elegy of the End",
        "Crimson Moon's Semblance"
    ]
}

# There are 4 ways to remove items from a dictionary

# 1) pop()
# Removes the item with the specified key name
print("Using the pop() method to remove the \"isLearningPython\" key from dictionary a")
print(a)
a.pop("isLearningPython")
print(a)

# 2) popitem()
# Removes the last inserted item (Before Python 3.7, a random item was removed instead due to dictionaries being unordered then)
print("Using the popitem() method to remove the last item of dictionary a")
print(a)
a.popitem()
print(a)

# 3) The del keyword
# Removes the item with the specified key name
print("Using the del keyword to remove the \"username\" key")
print(a)
del a["username"]
print(a)
# The del keyword can also be used to delete the entire dictionary
# del a # If dictionary a were to be printed after this statement, an error would be thrown as dictionary a no longer exists

# 4) clear()
# Empties the dictionary
print("Emptying dictionary a with the clear() method")
print(a)
a.clear()
print(a)