# Multiple values to multiple variables
# The number of variables must match the number of values, or else you will get an error.
a, b, c = "a", "b", "c"
print(a)
print(b)
print(c)

# One value to multiple variables
d = e = f = "String"
print(d)
print(e)
print(f)

# Unpacking a collection
# The process of extracting the collection of values in a list/tuple is called unpacking.
fruits = ["Apple", "Banana", "Cherry"]
g, h, i = fruits
print(g)
print(h)
print(i)