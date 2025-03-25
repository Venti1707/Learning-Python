a = {
    "name": "Nic",
    "favouriteWeapons": [
        "Elegy of the End",
        "Crimson Moon's Semblance"
    ]
}

# You can add an item to a dictionary by using a new index key and assigning a value to it
print("Adding the age value to dictionary a")
print(a)
a["age"] = 22
print(a)

# You can also use the update() method which takes in an iterable object with key:value pairs
print("Using the update() method to add the username key in dictionary a")
print(a)
a.update({"username": "Venti1707"})
print(a)