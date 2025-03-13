# There are 11 methods for lists in Python, these are

# 1) list.append(element)
# Adds an element at the end of the list
# element - An element of any data type
# Refer to the 4 - AddingItems.py file in this folder to see how to use this method

# 2) list.clear()
# Removes all the elements from the list
# Refer to 5 - RemovingItems.py in this folder to see how to use this method

# 3) list.copy()
# Returns a copy of the list
# Refer to 9 - Copying.py in this folder to see how to use this method

# 4) list.count(value)
# Returns the number of elements with the specified value
# value - The value to search for (is case sensitive) and is of any data type
a = "Banana"
print("Using the count() method to count the number of instances of " + a)
b = ["Apple", "Banana", "Cherry", "banana", "Banana"]
print(b.count(a))

# 5) list.extend(iterable)
# Add the elements of a list (or any iterable), to the end of the current list
# iterable - Any iterable (Like a list, set, tuple)
# Refer to 4 - AddingItems.py in this folder to see how to use this method

# 6) list.index(element)
# Returns the index of the first element with the specified value
# element - The element to search for and is of any data type
print("Using the index() method to find the index of the first instance of " + a)
print(b.index(a))

# 7) list.insert(position, element)
# Adds an element at the specified position
# position - A number specifying in which position to insert the value
# element - An element of any data type
# Refer to 4 - AddingItems.py in this folder to see how to use this method

# 8) list.pop(position)
# Removes the element at the specified position
# position - A number specifying the position of the element you want to remove, default value is -1, which returns the last item
# Refer to 5 - RemovingItems.py in this folder to see how to use this method

# 9) list.remove(element)
# Removes the item with the specified value
# element - The element to remove and is of any data type
# Refer to 5 - RemovingItems.py in this folder to see how to use this method

# 10) list.reverse(element)
# Reverses the order of the list
# Refer to 8 - Sorting.py in this folder to see how to use this method

# 11) list.sort(reverse = True|False, key = function)
# Sorts the list
# reverse - Default is False, which sorts the list in the ascending order
# key - A function to specify the sorting criteria
# Refer to 8 - Sorting.py in this folder to see how to use this method