a = ["Cherry", "Apple", "Elderberry", "Fig", "Berry", "Durian"]
b = [17, 7, 1707, 2003]

# You can sort lists using the sort() method
# The sort() method sorts alphanumerically in ascending order as a default
print("Sorting the default way - Alphanumerical, ascending order")
a.sort()
print(a)
b.sort()
print(b)

# To sort in descending order use the following keyword argument: reverse = True
print("Sorting the reverse way - Alphanumerical, descending order")
a.sort(reverse = True)
print(a)
b.sort(reverse = True)
print(b)

# You can customise the sort function by using the key = function keyword argument
# The function must return a number that will be used for sorting the list (The lowest number will be first)
print("Sorting based on how close the numbers are to 1000")
def closeTo1000(n):
    return abs(n - 1000)
b.sort(key = closeTo1000)
print(b)

# The sort() method is case sensitive, so all upper case letters will be sorted before lower case letters
print("Sorting is case sensitive, so all upper case letters will be sorted before lower case letters")
c = ["cherry", "Apple", "Elderberry", "fig", "Berry", "Durian"]
c.sort()
print(c)
# To make a sort function that is case insensitive, we can use the str.lower function as a key
print("Sorting is now case insensitive as str.lower is the key")
c.sort(key = str.lower)
print(c)

# To reverse a list regardless of the alphabet, use the reverse() method
print("Reversing list c, regardless of case sensitivity")
c.reverse()
print(c)