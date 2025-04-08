# If a is a dictionary, and b is an empty variable, you cannot simply do b = a to copy dictionary a
# This is because b will be a reference to a, so any changes done to a will be done to b as well
# As such, the only method to copy a dictionary is to use the built in copy() method for dictionaries
print("Using the copy() method to copy dictionary a")
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
b = a.copy()
print(b)

# You can also use the dict() function
print("Using the dict() function to copy dictionary b")
c = dict(b)
print(c)