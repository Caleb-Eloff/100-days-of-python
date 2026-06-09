import random
# This code imports the random module, which provides functions for generating random numbers
#  and performing random operations.

friends = ["Alice", "Bob", "Charlie", "David", "Emmanuel"]
random_friend = random.choice(friends)
print(random_friend)

# The choice function from the random module selects a random item from a list. In this case, it will select a
# random name from the friends list and print it. Each time you run the code, it may print a different name
# from the list.