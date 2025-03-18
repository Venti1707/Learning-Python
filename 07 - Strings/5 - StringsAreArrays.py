# Strings are arrays of bytes representing Unicode characters
# A character is not a data type
# As such, a single character is a string with length of 1
# Square brackets can be used to access elements of the string
a = "Hello world"
print(a[0]) # Get the first character
print(a[1]) # Get the second character

# To loop through the characters of the string, we can use a for loop
for i in a:
    print(i)