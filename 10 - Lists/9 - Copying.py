# Copying a list is not as simple as it looks
# Doing list1 = list2 will not work because if list1 changes, list2 changes alongside it
# The first way to copy a list is to use the copy() method
print("Using the copy() method to copy a method")
a = ["Apple", "Banana", "Cherry"]
b = a.copy()
if (a == b):
    print("b is the same list as a")
else:
    print("b is not the same list as a")

# Another way is to use the list() method
print("Using the list() method to copy a list")
c = list(b)
if (c == a):
    print("c is the same list as a")
else:
    print("c is not the same list as a")

# Another way is to use the slice operator (:)
print("Using the slice operator to copy a list")
d = c[:]
if (d == a):
    print("d is the same list as a")
else:
    print("d is not the same list as a")