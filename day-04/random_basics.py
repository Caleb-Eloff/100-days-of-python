import random
# Importing the random module allows us to use functions that generate random numbers.

random_integer = random.randint(1, 10)
print(random_integer)
# The randint function generates a random integer between the two specified numbers, inclusive.
# In this case, it will generate a random integer between 1 and 10.

random_number_0_to_1 = random.random()
print(random_number_0_to_1)
# The random function generates a random float between 0.0 and 1.0 inclusive of 0.0 but not 1.0.

random_float = random.uniform(1, 10)
print(random_float)
# The uniform function generates a random float between the two specified numbers, inclusive.