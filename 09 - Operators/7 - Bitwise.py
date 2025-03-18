# These operators are used to compare numbers (in binary)
a = 22 # 10110 in binary
b = 7 # 00111 in binary

# 1) variableName & value
# This is the bitwise AND operator which works as follows:
# Find the binary for both variableName & value
# Perform an AND for each value in each bit
# 0 & 0 = 0
# 0 & 1 = 0
# 1 & 0 = 0
# 1 & 1 = 1
print("variableName & value")
print(a & b)

# 2) variableName | value
# This is the bitwise OR operator which works as follows:
# Find the binary for both variableName & value
# Perform an OR for each value in each bit
# 0 | 0 = 0
# 0 | 1 = 1
# 1 | 0 = 0
# 1 | 1 = 1
print("variableName | value")
print(a | b)

# 3) variableName ^ value
# This is the bitwise XOR operator which works as follows:
# Find the binary for both variableName & value
# Perform a XOR for each value in each bit
# 0 ^ 0 = 0
# 0 ^ 1 = 1
# 1 ^ 0 = 1
# 1 ^ 1 = 0
print("variableName ^= value")
print(a ^ b)

# 4) ~variableName
# This is the bitwise NOT operator which works as follows:
# Find the binary for variableName
# Perform a NOT for each value in each bit
# ~0 = 1
# ~1 = 0
print("~variableName")
print(~a)

# 5) variableName >> value
# Shifts bits to the right, effectively dividing by powers of 2
# Floor division for positive numbers
# The final result would be variableName // (2 ** value)
print("variableName >> value")
print(a >> 2) # 22 / (2 ** 2) = 5.5; 5.5 floored is 5

# 6) variableName << value
# Shifts bits to the left, effectively multiplying by powers of 2
# The final result would be variableName * (2 ** value)
print("variableName << value")
print(a << b) # 22 * (2 ** 7) = 22 * 128 = 2816