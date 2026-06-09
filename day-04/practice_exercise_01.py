import random
# This code imports the random module, which provides functions for generating random numbers
#  and performing random operations.

coin_side = random.randint(0, 1)
if coin_side == 0:
    print("Heads")
else:
    print("Tails")

# The randint function generates a random integer between the two specified numbers, inclusive.
# In this case, it will generate either 0 or 1. If the generated number is 0, it prints "Heads".
# If the generated number is 1, it prints "Tails".