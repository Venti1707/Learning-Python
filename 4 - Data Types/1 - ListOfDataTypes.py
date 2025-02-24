# There are 8 data types in Python.

# 1. Text Type
print("Text Type - str")
a = "Hello world!"
print(type(a)) # str

# 2. Numeric Types
print("Numeric Type - int")
b = 20
print(type(b)) # int

print("Numeric Type - float")
c = 20.5
print(type(c)) # float

print("Numeric Type - complex")
d = 1j
print(type(d)) # complex

# 3. Sequence Types
print("Sequence Type - list")
e = ["Apple", "Banana", "Cherry"]
print(type(e)) # list

print("Sequence Type - tuple")
f = ("Apple", "Banana", "Cherry")
print(type(f)) # tuple

g = range(6)
print(type(g)) # range

# 4. Mapping Type
print("Mapping Type - dict")
h = {"name" : "Nic", "age" : 22}
print(type(h)) # dict

# 5. Set Types
print("Set Type - set")
i = {"Apple", "Banana", "Cherry"}
print(type(i)) # set

print("Set Type - frozenset")
j = frozenset({"Apple", "Banana", "Cherry"})
print(type(j)) # frozenset

# 6. Boolean Type
print("Boolean Type - bool")
k = True
print(type(k)) # bool

# 7. Binary Types
print("Binary Type - bytes")
m = b"Hello"
print(type(m)) # bytes

print("Binary Type - bytearray")
n = bytearray(5)
print(type(n)) # bytearray

print("Binary Type - memoryview")
o = memoryview(bytes(5))
print(type(o) ) # memoryview

# 8. None Type
print("None Type")
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