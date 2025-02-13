# There are 8 data types in Python.

# 1. Text Type
a = "Hello world"
print(type(a)) # str

# 2. Numeric Types
b = 20
print(type(b)) # int

c = 20.5
print(type(c)) # float

d = 1j
print(type(d)) # complex

# 3. Sequence Types
e = ["apple", "banana", "cherry"]
print(type(e)) # list

f = ("apple", "banana", "cherry")
print(type(f)) # tuple

g = range(6)
print(type(g)) # range

# 4. Mapping Type
h = {"name" : "Nic", "age" : 22}
print(type(h)) # dict

# 5. Set Types
i = {"apple", "banana", "cherry"}
print(type(i)) # set

j = frozenset({"apple", "banana", "cherry"})
print(type(j)) # frozenset

# 6. Boolean Type
k = True
print(type(k)) # bool

# 7. Binary Types
m = b"Hello"
print(type(m)) # bytes

n = bytearray(5)
print(type(n)) # bytearray

o = memoryview(bytes(5))
print(type(o) ) # memoryview

# 8. None Type
p = None
print(type(p)) # NoneType

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