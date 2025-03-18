# Slicing refers to returning a range of characters
# Slicing is done by specifying the start index and (end index + 1), separated by a colon (:)
# Syntax - variableName[startIndex:(endIndex + 1)]
# Note that the end index is not included in the slice
a = "Hello world!"
print("Slicing between a given start and a given end index")
print(a[1:5])

# To slice from the start, simply leave out the start index
# Syntax - variableName[:(endIndex + 1)]
# Like regular slicing, the end index is not included in the slice
print("Slicing between the start of the string and a given end index")
print(a[:5])

# To slice from the start, simply leave out the end index
# Syntax - variableName[startIndex:]
print("Slicing from a given start index to the end of the string")
print(a[1:])

# To slice from the back, use negative indexes
# The last character now has an index of -1
# Syntax - variableName[startIndex:endIndex] - startIndex and endIndex are negative integers
# Like regular slicing, the end index is not included in the slice
print("Slicing from the back")
print(a[-6:-1])