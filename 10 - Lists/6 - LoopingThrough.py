a = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Fig"]

# You can loop through lists with a for loop
print("Using a for loop to loop through items of a list")
for item in a:
    print(item)

# You can also make use of the index number
print("Using a for loop to loop through the indexes of items of a list")
for index in range(len(a)):
    print("Index " + str(index) + ": " + a[index])

# You can also loop through lists with a while loop
print("Using a while loop to loop through items of a list")
whileIndex = 0
while whileIndex < len(a):
    print("whileIndex " + str(whileIndex) + ": " + a[whileIndex])
    whileIndex += 1

# You can also use list comprehension, which is the shortest way, syntax wise
print("Using list comprehension to loop through items of a list")
[print(listComprehensionIndex) for listComprehensionIndex in a]