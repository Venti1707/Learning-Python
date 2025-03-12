a = ["Apple", "Banana", "Cherry"]
b = ["Durian", "Elderberry", "Fig"]

# There are multiple ways to join lists
# The 1st way is to use the + operator
print("Using the + operator to join list a & b")
c = a + b
print(c)

# The 2nd way is to append the items from one list to another, one item at a time
print("Using a for loop to append items from list b to list a, one item at a time")
for item in b:
    a.append(item)

print(a)

a = ["Apple", "Banana", "Cherry"]

# The last way is to use the extend() method which takes in the list that is to be joined to the first list
print("Using the extend() method to join list b to list a")
d = a.extend(b)
print(d)