# Accessing items in tuples is similar to that of accessing items in tuples
a = ("Apple", "Banana", "Cherry", "Durian", "Elderberry", "Fig")

# Tuple items are indexed and you can refer to the index number
# The index number starts with 0
print("Getting the first item of tuple a")
print(a[0])

# Negative indexing is getting items from a tuple from the back
print("Getting the last item of tuple a")
print(a[-1])

# To get a range of values, specify it within square braces as follows tupleName[startIndex:endIndex]

# endIndex is not included in the returned value, so the range of values is from startIndex to (endIndex - 1)
# If startIndex is not specified, it is set to the start of the tuple
print("From the front; Getting every item from the 1st to 4th item of tuple a")
print(a[:5])

# If endIndex is not specified, it is set to the end of the tuple
print("From the front; Getting every item from the 2nd to last item of tuple a")
print(a[1:])

# If you use negative indexes, you are searching from the back of the tuple
print("From the back; Getting the 4th item to the second to last item of the tuple")
print(a[-4:-1])

# To check if an item exists in a tuple, use the in keyword
print("Checking if an item exists in a tuple")
if "Durian" in a:
    print("Yes, Durian is in tuple a")