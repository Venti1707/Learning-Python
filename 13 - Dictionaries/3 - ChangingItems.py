a = {
    "name": "Nic",
    "age": 21,
    "username": "Venti170",
    "favouriteWeapons": [
        "Elegy of the End",
        "Crimson Moon's Semblance"
    ]
}

# You can change the value of a specific item by referring to its key name
print("Changing the value of the age key in dictionary a")
print(a)
a["age"] = 22
print(a)

# You can also use the update() method which takes in an iterable object with key:value pairs
print("Using the update() method to update the username key in dictionary a")
print(a)
a.update({"username": "Venti1707"})
print(a)