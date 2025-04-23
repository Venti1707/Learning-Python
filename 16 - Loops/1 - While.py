# The while loop is used to execute a set of statements as long as a condition is true
# The while loop requires variables to be defined before the loop
# The general syntax is as follows:
# Variable declaration
#
# while (condition):
#     code to be executed

print("Example of a while loop")
a = 1
while (a <= 6):
    print(a)
    a += 1

# The break keyword can be used to stop the loop when the condition has been fulfilled
print("Example of a while loop with the break keyword")
b = 1
while (b <= 6):
    print(b)
    if (b == 3):
        break
    b += 1

# The continue keyword can be used to stop the current iteration of the loop and continue with the next
print("Example of a while loop with the continue keyword")
c = 1
while (c <= 6):
    c += 1
    if (c == 3):
        continue
    print(c)

# The else keyword can be used to run a code block once the loop is finished
print("Example of a while loop with the else keyword")
d = 1
while (d <= 6):
    print(d)
    d += 1
else:
    print("d is no longer less than or equal to 6")