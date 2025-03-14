a = ("Apple", "Banana", "Cherry", "Durian", "Elderberry", "Fig")

# You can loop through tuples with a for loop
print("Using a for loop to loop through items of a tuple")
for item in a:
    print(item)

# You can also make use of the index number
print("Using a for loop to loop through the indexes of items of a tuple")
for index in range(len(a)):
    print("Index " + str(index) + ": " + a[index])

# You can also loop through tuples with a while loop
print("Using a while loop to loop through items of a tuple")
whileIndex = 0
while whileIndex < len(a):
    print("whileIndex " + str(whileIndex) + ": " + a[whileIndex])
    whileIndex += 1