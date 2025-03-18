# To check if a certain phrase or character is present in a string, the in keyword can be used
a = "Hello world"
print("world" in a)

# Use an if statement instead of returning True/False
if "worlds" in a:
    print("worlds is inside", a)
else:
    print("worlds is not inside", a)

# To check if a certain phrase or character is NOT present in a string, the not keyword can be used in conjunction with the in keyword
if "Goodbye" not in a:
    print("Goodbye is not inside", a)
else:
    print("Goodbye is inside", a)