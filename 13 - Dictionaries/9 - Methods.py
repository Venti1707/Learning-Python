# There are 11 methods for dictionaries in Python, these are
# 1) dictionary.clear()
# Removes all the elements from the dictionary
# Refer to 5 - RemovingItems.py in this folder to see how to use this method

# 2) dictionary.copy()
# Returns a copy of the dictionary
# Refer to 7 - Copying.py in this folder to see how to use this method

# 3) dictionary.fromkeys(key, value)
# Returns a dictionary with the specified keys and value
# key - An iterable specifying the keys of the new dictionary; Required
# value - The value for all keys; Default value is None
a = ("Venti", "Arlecchino")
b = dict.fromkeys(a)
print("Making a new dictionary with the fromkeys() method")
print(b)

# 4) dictionary.get()
# Returns the value of the specified key
# Refer to 2 - AccessingItems.py in this folder to see how to use this method

# 5) dictionary.items()
# Returns a list containing a tuple for each key value pair
# Refer to 6 - LoopingThrough.py in this folder to see how to use this method


# 6) dictionary.keys()
# Returns a list containing the dictionary's keys
# Refer to 6 - LoopingThrough.py in this folder to see how to use this method

# 7) dictionary.pop()
# Removes the element with the specified key
# Refer to 5 - RemovingItems.py in this folder to see how to use this method

# 8) dictionary.popitem()
# Removes the last inserted key-value pair
# Refer to 5 - RemovingItems.py in this folder to see how to use this method

# 9) dictionary.setdefault(keyName, value)
# Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# keyName - The keyname of the item you want to return the value from; Required
# value - The value of the key if the key does not exist. If the key exists, this parameter has no effect; Default value is None
d = {
    "name": "Nic",
    "username": "Venti1707",
    "isLearningPython": True,
    "favouriteWeapons": [
        "Elegy of the End",
        "Crimson Moon's Semblance"
    ]
}
print("Setting the value of the age key in dictionary d")
print(d)
e = d.setdefault("age", 22)
print(d)

# 10) dictionary.update()
# Updates the dictionary with the specified key-value pairs
# Refer to 3 - ChangingItems.py in this folder to see how to use this method

# 11) dictionary.values()
# Returns a list of all the values in the dictionary
# Refer to 2 - AccessingItems.py in this folder to see how to use this method