# int()
# 1. Constructs an integer number from an integer literal
# 2. A float literal (By removing all decimals)
# 3. A string literal (Providing the string represents a whole number)
a = int(1.61803398874989) # a will be 1
b = int(2.718281828459045235360287471352) # b will be 2
c = int("-3") # c will be -3

print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))