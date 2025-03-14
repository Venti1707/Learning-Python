# When assigning values to a tuple is also known as "packing" a tuple
a = ("Apple", "Banana", "Cherry")
# Extracting values back into variables is known as "unpacking"
print("\"Unpacking\" the values in tuple a where the number of variables match the number of values in the tuple")
(green, yellow, red) = a
print(green)
print(yellow)
print(red)

# The number of variables must match the number of values in the tuple
# If they do not, an asterisk (*) has to be used to collect the remaining values as a list
print("\"Unpacking\" the values in tuple b where the number of variables do not match the number of values in the tuple")
b = ("Apple", "Banana", "Cherry", "Dragonfruit")
(green, yellow, *red) = b
print(green)
print(yellow)
print(red)

# If the asterisk is added to variable names that is not the last,
# the values will be assigned until the number of values matches the number of variables
print("\"Unpacking\" the values in tuple c where the asterisked variable is not the last")
c = ("Apple", "Banana", "Lemon", "Cherry")
(green, *yellow, red) = c
print(green)
print(yellow)
print(red)