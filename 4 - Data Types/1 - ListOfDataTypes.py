# There are 8 data types in Python.
# Text Type: str
# Numeric Types: int, float, complex
# Sequence Types: list, tuple, range
# Mapping Type: dict
# Set Types: set, frozenset
# Boolean Type: bool
# Binary Types: bytes, bytearray, memoryview
# None Type: NoneType

a = "Hello world"
print(type(a))

b = 20
print(type(b))

c = 20.5
print(type(c))

d = 1j
print(type(d))

e = ["apple", "banana", "cherry"]
print(type(e))

f = ("apple", "banana", "cherry")
print(type(f))

g = range(6)
print(type(g))

h = {"name" : "Nic", "age" : 22}
print(type(h))

i = {"apple", "banana", "cherry"}
print(type(i))

j = frozenset({"apple", "banana", "cherry"})
print(type(j))

k = True
print(type(k))

m = b"Hello"
print(type(m))

n = bytearray(5)
print(type(n))

o = memoryview(bytes(5))
print(type(o))

p = None
print(type(p))

# To specify the data type, use the respective constructor functions which are as follows
# str()
# int()
# float()
# complex()
# list()
# tuple()
# range()
# dict()
# set()
# frozenset()
# bool()
# bytes()
# bytearray()
# memoryview()