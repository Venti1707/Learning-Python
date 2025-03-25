a = {
    "name": "Nic",
    "username": "Venti1707",
    "favouriteWeapons": [
        "Elegy of the End",
        "Crimson Moon's Semblance"
    ]
}

# To get the specified value in a dictionary, use square brackets surrounded by the key, which is to be surrounded by inverted commas (")
print("Getting the value of the \"username\" key")
print(a["username"])
# You can also use the get() method
print("Using the get() method to get the value of the \"username\" key")
b = a.get("username")
print(b)

# To get all the keys in the dictionary, use the keys() method
print("Using the keys() method to get all the keys in dictionary a")
c = a.keys()
print(c)

# The keys printed out earlier will be updated if there are any changes done to the dictionary
print("The outdated keys in dictionary a")
print(c)
print("The updated keys in dictionary a")
a["age"] = 21
print(c)

# To get all the values in the dictionary, use the values() method
print("Using the values() method to get all the values in dictionary a")
d = a.values()
print(d)

# The values printed out earlier will be updated if there are any changes done to the dictionary
print("The outdated values in dictionary a")
print(d)
print("The updated values in dictionary a")
a["age"] = 22
print(d)

# To get all the items in the dictionary, use the items() method
print("Using the values() method to get all the values in dictionary a")
e = a.items()
print(e)

# The items printed out earlier will be updated if there are any changes done to the dictionary
print("The outdated items in dictionary a")
print(e)
print("The updated items in dictionary a")
a["isLearningPython"] = True
print(e)

# To check if a key exists in a dictionary, use the in keyword
print("Using the in keyword to see if the key \"favouriteWeapons\" is inside dictionary a")
if ("favouriteWeapons" in a):
    print("\"favouriteWeapons\" is inside dictionary a")
else:
    print("\"favouriteWeapons\" is not inside dictionary a")