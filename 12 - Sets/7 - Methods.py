# There are 17 methods for sets in Python, these are
# 1) set.add()
# Adds an element to the set
# Refer to 3 - AddingItems.py in this folder to see how to use this method

# 2) set.clear()
# Removes all the elements from the set
a = {"Apple", "Banana", "Cherry"}
print("Using clear() to clear set a")
print(a)
a.clear()
print(a)

# 3) set.copy()
# Returns a copy of the set
# Refer to 6 - Joining.py in this folder to see how to use this method

# 4) set.difference_update()
# Removes the items in this set that are also included in another, specified set
# Refer to 6 - Joining.py in this folder to see how to use this method

# 5) set.difference()
# Returns a set containing the difference between two or more sets
# Refer to 6 - Joining.py in this folder to see how to use this method

# 6) set.discard()
# Removes the specified item
# Refer to 4 - RemovingItems.py in this folder to see how to use this method

# 7) set.intersection_update()
# Removes the items in this set that are not present in other, specified sets
# Refer to 6 - Joining.py in this folder to see how to use this method

# 8) set.intersection()
# Returns a set, that is the intersection of two other sets
# Refer to 6 - Joining.py in this folder to see how to use this method

# 9) set1.isdisjoint(set2)
# Returns a Boolean value on whether set1 and set2 have a intersection or not
# set2 - The set to search for equal items in
print("Using the isdisjoint() method to see if b and c have any intersections")
b = {"Apple", "Banana", "Cherry"}
c = {"Durian", "Elderberry", "Fig"}
print(b.isdisjoint(c))

# 10) set1.issubset(set2)
# Returns a Boolean value on whether set2 contains set1 or not
# Shortcut is the <= operator
# set2 - The set to search for equal items in
d = {"Apple", "Banana", "Cherry"}
e = {"Cherry"}
f = {"Apple", "Banana"}
print("Using the issubset() method to see if e is a subset of d")
print(e.issubset(d))
print("Using the <= operator to see if e is a subset of d")
print(e <= d)
# There is also the < operator, which checks if it is a proper subset
# A proper subset indicates the following:
# 1) All elements of the set on the left are in the set on the right
# 2) Not all elements in the set on the right are in the left
print("Using the < operator to see if e is a proper subset of d")
print(e < d)

# 11) set1.issuperset(set2)
# Returns a Boolean value on whether set1 contains set2 or not
# Shortcut is the <= operator
# set2 - The set to search for equal items in
print("Using the issubset() method to see if e is a subset of d")
print(d.issuperset(e))
print("Using the >= operator to see if e is a subset of d")
print(d >= e)
# There is also the > operator, which checks if it is a proper superset
# A proper subset indicates the following:
# 1) All elements of the set on the right are in the set on the right
# 2) Not all elements in the set on the left are in the right
print("Using the > operator to see if d is a proper subset of e")
print(d > e)

# 12) pop()
# Removes an element from the set
# Refer to 4 - RemovingItems.py in this folder to see how to use this method

# 13) remove()
# Removes the specified element
# Refer to 4 - RemovingItems.py in this folder to see how to use this method

# 15) symmetric_difference_update()
# Inserts the symmetric differences from this set and another
# Refer to 6 - Joining.py in this folder to see how to use this method

# 16) symmetric_difference()
# Returns a set with the symmetric differences of two sets
# Refer to 6 - Joining.py in this folder to see how to use this method

# 17) union()
# Return a set containing the union of sets
# Refer to 6 - Joining.py in this folder to see how to use this method

# 18) update()
# Update the set with the union of this set and others
# Refer to 3 - AddingItems.py or 6 - Joining.py in this folder to see how to use this method