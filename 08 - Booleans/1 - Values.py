# Booleans can only represent 1 of 2 values: True or False
# When 2 values are compared, the expression is evaluated and a Boolean value is returned
a = 10
b = 9
print("a < b")
print(a < b)
print("a <= b")
print(a <= b)
print("a == b")
print(a == b)
print("a > b")
print(a > b)
print("a >= b")
print(a > b)

# The bool() function can evaluate any value and will return a Boolean value
# Almost every value is evaluated to True if it has some sort of content
# Every string except empty strings is True
# Values such as (), [], {}, 0, the value None all evaluate to False
print("Strings")
c = "Hello world!"
d = ""
print(bool(c))
print(bool(d))

print("Integers")
f = 22
g = 0
print(bool(f))
print(bool(g))

print("Tuples")
h = ("Apple", "Banana", "Cherry")
i = ()
print(bool(h))
print(bool(i))

print("Lists")
j = ["Apple", "Banana", "Cherry"]
k = []
print(bool(j))
print(bool(k))

print("Dictionaries")
l = {"Apple", "Banana", "Cherry"}
m = {}
print(bool(l))
print(bool(m))

print("Other values")
n = None
o = False
print(bool(n))
print(bool(o))

# Functions can return a Boolean value
print("Functions")
def returnTrue() :
  return True
print(returnTrue())

# This can be then implemented into an if logic
if returnTrue():
  print("Yes it's true")
else:
  print("No it's false")

# There are built in functions within Python which return Boolean values