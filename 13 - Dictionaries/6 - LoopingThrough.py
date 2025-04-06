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
# To loop through keys/values of a dictionaries, use a for loop
print("Looping through keys of a dictionary with a for loop")
for key in a:
    print(key)

print("Looping through values of a dictionary with a for loop")
for value in a:
    print(a[value])

# The keys()/values() method can also be used to return the keys/values of the dictionary
print("Looping through keys of a dictionary with the keys() method")
for keys in a.keys():
    print(keys)

print("Looping through values of a dictionary with the values() method")
for values in a.values():
    print(values)

# To return both keys and values of a dictionary, use the items() method
print("Looping through both keys and values of a dictionary with the items() method")
for items in a.items():
    print(items)