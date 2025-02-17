# There is no function called random() to generate random numbers
# We have to use the built in module named random to generate them instead
import random
lowerBound = 1 # The minimum value it would generate
upperBound = 10 # The maximum value + 1 it would generate
print(random.randrange(lowerBound, upperBound)) # Generate a random number between 1 to 9