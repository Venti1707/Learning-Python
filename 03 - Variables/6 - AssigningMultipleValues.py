# Multiple values to multiple variables
# The number of variables must match the number of values, or you will get an error
print("Multiple values to multiple variables")
a, b, c = "a", "b", "c"
print(a)
print(b)
print(c)

# One value to multiple variables
print("One value to multiple variables")
d = e = f = "String"
print(d)
print(e)
print(f)

# Unpacking a collection
# The process of extracting the collection of values in a list/tuple is called unpacking
print("Unpacking a collection")
fruits = ["Apple", "Banana", "Cherry"]
g, h, i = fruits
print(g)
print(h)
print(i)