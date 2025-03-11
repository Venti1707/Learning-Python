a = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Fig"]

# To change the value of a single item, simply overwrite it with its corresponding index number
print("Changing the 2nd item in list a")
print(a)
a[1] = "Berry"
print(a)

# To change a range of values, specify the range and define a list with the new values
print("Changing a range of values in list a")
print(a)
a[1:3] = ["Banana", "Cantaloupe"]
print(a)

# If you insert more items than you replace, the new items will be inserted where they are specified
# The remaining items will then move accordingly
print("Inserting more items than replaced in list a")
print(a)
a[1:2] = ["Berry", "Banana"]
print(a)

# If you insert fewer items than you replace, the new items will be inserted where they are specified
# The remaining items will then move accordingly
print("Inserting fewer items than replaced in list a")
print(a)
a[1:4] = ["Banana", "Cherry"]
print(a)