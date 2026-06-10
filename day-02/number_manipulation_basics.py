bmi = 84 / 1.65 ** 2

print(int(bmi))
# Output: 30.85399449035813

print(round(bmi))
# Output: 31
# The int() function truncates the decimal part of the number,
# while the round() function rounds the number to the nearest 
# integer.

print(round(bmi, 2))
# Output: 30.85
# The round() function rounds a number to a specified number of
# decimal places. If the second argument is omitted, it rounds to
# the nearest integer. In this case, we round the BMI value to 2
# decimal places for a more precise representation.

score = 0
score += 1
print(score)
# Output: 1
# The += operator is a shorthand for adding a value to a variable
# and assigning the result back to that variable.

height = 1.65
is_winning = True
print(f"Your score is {score}, height is {height} and you are winning is {is_winning}")