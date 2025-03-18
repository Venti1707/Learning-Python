# Conversion from one type to another is possible with the int(), float(), and complex() methods
a = 1 # int
b = 2.7 # float
c = 3 - 1j # complex

# Converting from int to float
d = float(a)
print(type(d))

# Converting from float to int
e = int(b)
print(type(e))

# Converting from int to complex
f = complex(a)
print(type(f))