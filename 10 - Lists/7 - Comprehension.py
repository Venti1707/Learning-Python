# List comprehension is a shorter syntax for creating new lists based on values on an existing list
a = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Fig"]

# If we want to make a new list where the elements are elements of a that contain the letter "A"/"a"
# we can use a for loop together with an if statement
print("Using a for loop and an if statement")
b = []
for index in a:
    if (("a" in index) or ("A" in index)):
        b.append(index)
print(b)

# With list comprehension, this can be done in a single line
print("Using list comprehension")
c = [index.upper() for index in a if (("a" in index) or ("A" in index))]
print(c)

# The general syntax for a list comprehension is as follows
# newList = [(expression) for (item) in (iterable) if ((condition) == True)]
# expression has to make use of the item and is also the final outcome, so it can be manipulated
# It can also contain conditional statements as a way to manipulate the outcome
# iterable can be any iterable object, like a list, tuple, set
# condition acts like a filter that only accepts items that evaluate to True; It can also be omitted