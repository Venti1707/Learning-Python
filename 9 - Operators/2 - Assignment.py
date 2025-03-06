# These operators are used to assign values to variables

# 1) variableName = value
print("variableName = value")
a = 1
print(a)

# 2) variableName += value
# Same as variableName = variableName + value
print("variableName += value")
b = 2
b += 3
print(b)

# 3) variableName -= value
# Same as variableName = variableName - value
print("variableName -= value")
c = 3
c -= 4
print(c)

# 4) variableName *= value
# Same as variableName = variableName * value
print("variableName *= value")
d = 5
d *= 6
print(d)

# 5) variableName /= value
# Same as variableName = variableName / value
print("variableName /= value")
e = 7
e /= 8
print(e)

# 6) variableName %= value
# Same as variableName = variableName % value
print("variableName %= value")
f = 9
f %= 10
print(f)

# 7) variableName //= value
# Same as variableName = variableName // value
print("variableName //= value")
g = 11
g //= 12
print(g)

# 8) variableName **= value
# Same as variableName = variableName ** value
print("variableName **= value")
h = 13
h **= 14
print(h)

# 9) variableName &= value
# Same as variableName = variableName & value
# This is the bitwise AND operator which works as follows:
# Find the binary for both variableName & value
# Perform an AND for each value in each bit
# 0 & 0 = 0
# 0 & 1 = 0
# 1 & 0 = 0
# 1 & 1 = 1
print("variableName &= value")
i = 15 # The binary for i is 01111
i &= 16 # The binary for 16 is 10000
print(i) # When they are "AND", the value is 00000 in binary, or 0 in decimal

# 10) variableName |= value
# Same as variableName = variableName | value
# This is the bitwise OR operator which works as follows:
# Find the binary for both variableName & value
# Perform an OR for each value in each bit
# 0 | 0 = 0
# 0 | 1 = 1
# 1 | 0 = 0
# 1 | 1 = 1
print("variableName |= value")
j = 17 # The binary for j is 10001
j |= 18 # The binary for 18 is 10010
print(j) # When they are "OR", the value is 10011 in binary, or 19 in decimal

# 11) variableName ^= value
# Same as variableName = variableName ^ value
# This is the bitwise XOR operator which works as follows:
# Find the binary for both variableName & value
# Perform a XOR for each value in each bit
# 0 ^ 0 = 0
# 0 ^ 1 = 1
# 1 ^ 0 = 1
# 1 ^ 1 = 0
print("variableName ^= value")
k = 19 # The binary for k is 10011
k ^= 20 # The binary for 20 is 10100
print(k) # When they are "XOR", the value is 000111

# 12) variableName >>= value
# Same as variableName = variableName >> value
# Shifts bits to the right, effectively dividing by powers of 2
# Floor division for positive numbers
# The final result would be variableName // (2 ** value)
print("variableName >>= value")
l = 21 # The binary for l is 10101
l >>= 2 # Shift l by 2 bits
print(l) # 21 / (2 ** 2) = 5.25; 5.25 floored is 5

# 13) variableName <<= value
# Same as variableName = variableName << value
# Shifts bits to the left, effectively multiplying by powers of 2
# The final result would be variableName * (2 ** value)
print("variableName <<= value")
m = 22
m <<= 2
print(m) # 22 * (2 ** 2) = 22 * 4 = 88

# 14) variableName := value
# Same as
# variableName = value
# print(variableName)
print("variableName := value")
print(n := 23)