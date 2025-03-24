# Dictionaries are used to store data values in key:value pairs
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates
# *As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# Dictionaries are written with curly brackets, and have keys and values
# Values in dictionaries can be of any data type
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
print(a)

# To get the specified value in a dictionary, use square brackets surrounded by the key, which is to be surrounded by inverted commas (")
print("Getting the age value in dictionary a")
print(a["age"])

# You can also use the dict() constructor to construct a dictionary
print("Using the dict() constructor to construct a dictionary")
b = dict(name = "Nic", age = 22, username =  "Venti1707", isLearningPython = True, favouriteWeapons = ["Elegy of the End", "Crimson Moon's Semblance"])
print(b)

""""
| ---------- | -------- | ------------------ |--------------------------|
| Type       | Ordered? | Changeable?        | Allows duplicate members?|
| ---------- | -------- | ------------------ |--------------------------|
| List       | Yes      | Yes                | Yes                      |
| Tuple      | Yes      | Yes                | Yes                      |
| Set        | No       | No*, and unindexed | No                       |
| Dictionary | Yes**    | Yes                | No                       |

*Set items are unchangeable, but you can remove and/or add items whenever you like
**As of Python version 3.7, dictionaries are ordered; In Python 3.6 and earlier, dictionaries are unordered
"""