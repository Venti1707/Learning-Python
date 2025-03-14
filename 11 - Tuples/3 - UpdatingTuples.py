# Tuples are immutable - That is items cannot be changed, added or removed once the tuple is created
a = ("Apple", "Banana", "Cherry", "Durian", "Elderberry", "Fig")

# There is however a workaround to change the values of a tuple
# 1) Convert the tuple to a list
# 2) Change the items in the list
# 3) Change the list back to a tuple
print("Changing the value of the 2nd item in tuple a")
print(a)
b = list(a)
b[1] = "Berry"
a = tuple(b)
print(a)

# To append items to a tuple, do the "3 steps" method
print("Appending items to tuple a")
print(a)
c = list(a)
c.append("Grapes")
a = tuple(c)
print(a)

# To add a tuple to another tuple, use +=
print("Adding tuple d to tuple a")
print(a)
d = ("Honeydew", "Honeydew")
a += d
print(a)

# To remove an item from a tuple, do the "3 steps" method
print("Removing an item from list a")
print(a)
e = list(a)
e.remove("Honeydew")
a = tuple(e)
print(a)

# To remove the entire tuple, use the del keyword
# del a # This will produce an error if printed as tuple a no longer exists