# A dictionary that contain 1 or more dictionaries is called a nested dictionary
a = {
    "Venti": {
        "Element": "Anemo",
        "Weapon": "Bow",
        "Birthday": "16/6",
    },

    "Arlecchino": {
        "Element": "Pyro",
        "Weapon": "Polearm",
        "Birthday": "22/8"
    }
}

# You can also create the dictionaries individually, then create the nested dictionary which contains the individual dictionaries
b = {
    "Element": "Anemo",
    "Weapon": "Bow",
    "Birthday": "16/6"
}

c = {
    "Element": "Pyro",
    "Weapon": "Polearm",
    "Birthday": "22/8"
}

d = {
    "Venti": b,
    "Arlecchino": c
}
print("Using individual dictionaries to make a nested dictionary")
print(d)

# To access items within a nested dictionary, use the name of the dictionary, starting with the outer dictionary
print("Finding the value of Venti's birthday")
print(d["Venti"]["Birthday"])

# To loop through nested dictionaries, use the items() method
for e, f in d.items():
    print("Inner dictionary key: " + e)

    for g in f:
        print(g + ": " + f[g])