a = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Fig"]

# List items are indexed and you can refer to the index number
# The index number starts with 0
print("Getting the first item of list a")
print(a[0])

# Negative indexing is getting items from a list from the back
print("Getting the last item of list a")
print(a[-1])

# To get a range of values, specify it within square braces as follows listName[startIndex:endIndex]

# endIndex is not included in the returned value, so the range of values is from startIndex to (endIndex - 1)
# If startIndex is not specified, it is set to the start of the list
print("From the front; Getting every item from the 1st to 4th item of list a")
print(a[:5])

# If endIndex is not specified, it is set to the end of the list
print("From the front; Getting every item from the 2nd to last item of list a")
print(a[1:])

# If you use negative indexes, you are searching from the back of the list
print("From the back; Getting the 4th item to the second to last item of the list")
print(a[-4:-1])

# To check if an item exists in a list, use the in keyword
print("Checking if an item exists in a list")
if "Durian" in a:
    print("Yes, Durian is in list a")