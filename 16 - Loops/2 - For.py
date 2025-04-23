# The for loop is used to loop over iterables such as lists, tuples, sets, dictionaries and even strings
# This is less like the for keyword in other programming languages and works more like an iterator method
# With the for loop, we can execute a set of statements, once for each item in a list, tuple, set, dictionary or string

# For example, if we want to print each item in a list, we can do the following
print("Printing each item in a list using a for loop")
a = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Fig", "Grape"]
for b in a:
    print(b)

# If we want to print each character in a string, we can do the following
print("Example of a for loop")
for c in a[0]:
    print(c)

# Similar to a while loop, using the break keyword will stop the loop before it has finished looping through all the items
print("Example of a for loop with the break keyword after the print statement")
for d in a:
    print(d)
    if d == "Banana":
        break

# If the print statement is after the break statement, the output will be different
print("Example of a for loop with the break keyword before the print statement")
for e in a:
    if e == "Banana":
        break
    print(e)

# Similar to a for loop, the continue keyword can be used to stop the current iteration of the loop and continue with the next
print("Example of a for loop with the continue keyword")
for f in a:
    if f == "Banana":
        continue
    print(f)

# The range() function can be used with a for loop to loop through a set of code a specified number of times
# The range() function takes in 3 parameters
# parameter1 - The starting value; Default value is 0
# parameter2 - The ending value; Is not included in the final output
# parameter3 - The step; Default value is 1
print("Example of a for loop with the range() function")
for g in range(0, 11, 2):
    print(g)

# Similar to a while loop, the else keyword can be used to run a code block once the loop is finished
# The else block will not be executed if the loop is stopped by a break statement
print("Example of a for loop with the else keyword")
for h in range(11):
    print(h)
else:
    print("h is no longer less than 11")

# Nested loops are loops contained within loops
i = ["Big", "Tasty"]
j = ["Apple", "Banana", "Cherry" ]
for k in i:
    for l in j:
        print(k, l)

# As for loops cannot be empty, the pass keyword is used to avoid getting an error
print("Example of a for loop with the pass keyword")
for m in a:
    pass