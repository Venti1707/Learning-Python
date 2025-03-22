# There are 5 ways to join 2 or more iterables with a set in Python, separated by commas
a = {"Apple", "Banana"}
b = {"Cherry", "Durian"}
c = {"Elderberry", "Fig"}
d = ("Fig", "Grapes") # This will be converted into a set
e = ("Honeydew",) # This tuple will be used for some examples

# 1) union()
# Returns a set containing the union of all iterables involved
# Shortcut is the | operator
# Ignores all duplicates
print("Using the union() method to join iterables a, b, c, d and e")
f = a.union(b, c, d, e)
print(f)
print("Using the | operator to join sets a, b, c and d") # You can only join with sets when using the shortcut operator
g = a | b | c | set(d)
print(g)

# 2) update()
# Insert all items from one iterable to another
# Changes the original set, doesn't return a new set
# Ignores all duplicates
h = a.copy()
print("Using the update() method to join iterables h, b, c, d and e together")
print(h)
h.update(b, c, d, e)
print(h)

# 3) intersection()
# Returns a set that is the intersection of two or more iterables
# Shortcut is the & operator
print("Using the intersection() method to find common elements between c and d")
i = c.intersection(d)
print(i)
print("Using the & operator to find common elements between c and set(d)")
j = c & set(d)
print(j)

# 4) intersection_update()
# Removes the items in this set that are not present in two or more specified set(s)
# Shortcut is the &= operator
# Changes the original set, doesn't return a new set
k = set(d).copy()
print("Using the intersection_update() method to remove non-common elements between k and c")
k.intersection_update(c)
print(k)
print("Using the &= operator to remove non-common elements between l and c")
l = set(d).copy()
l &= c
print(l)

# 5) difference()
# Returns a set containing the difference between two or more iterables
# Shortcut is the - operator
print("Using the difference() method to find the difference between c and d")
m = c.difference(d)
print(m)
print("Using the - operator to find the difference between c and set(d)")
n = c - set(d)
print(n)

# 6) symmetric_difference()
# Returns a set with the the elements that are not in two iterables
# Shortcut is the ^ operator
print("Using the symmetric_difference() method to find the elements that are not in c and d")
o = c.symmetric_difference(d)
print(o)
print("Using the ^ operator to find the elements that are not in c and set(d)")
p = c ^ set(d)
print(p)

# 7) symmetric_difference_update()
# Inserts the symmetric differences from this set and another
# Shortcut is the ^= operator
# Changes the original set, doesn't return a new set
q = c.copy()
print("Using the symmetric_difference_update() method to find the elements that are not in q and d")
print(q)
q.symmetric_difference_update(d)
print(q)