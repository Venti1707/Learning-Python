# It is not possible to concatenate strings and numbers in Python
# To do so, F-strings has to be used
age = 22
text1 = f"My name is Nic and I am {age} years old this year"
print(text1)

# We can also use F-strings to modify the format of the variable
# For instance, adding a colon, followed by a legal formatting type (like .2f) means a fixed point number with 2 decimal places
phi = 1.61803398874989
text2 = f"Phi to 2 decimal places is {phi:.2f}"
print(text2)

# We can also use F-strings to evaluate Python code
e = 2.718281828459045
negativePi = -3.141592653589793
text3 = f"e + negativePi = {e + negativePi}"
print(text3)