a = {"Apple", "Banana", "Cherry"}
# To add items to to a set, use the add() method

# Adding an item to a set using the add() method
print("Adding items to set a using the add() method")
print(a)
a.add("Durian")
print(a)

# To add 1 iterable to a set, use the update() method
b = ["Fig"]
c = ("Grapes",)
d = {"Elderberry"}
print("Adding list b to set a using the update() method")
a.update(b)
print(a)
print("Adding tuple c to set a using the update() method")
a.update(c)
print(a)
print("Adding set d to set a using the update() method")
a.update(d)
print(a)