for number in range(1, 11):
    print(number)
# This code uses a for loop to iterate through a range of numbers from 1 to 10.
# The range function generates a sequence of numbers, and the for loop goes through each number in that sequence
# and prints it, non inclusive of the end value (11 in this case).

for number in range(1, 11, 2):
    print(number)
# This code uses a for loop to iterate through a range of numbers from 1 to 10, but it includes a step value of 2.
# This means that it will generate a sequence of numbers starting from 1, and then it will skip every second number, 
# resulting in the sequence 1, 3, 5, 7, 9.