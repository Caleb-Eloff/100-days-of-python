import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

temp_password = []
for letter in range(0, num_letters):
    temp_password += random.choice(letters)
for number in range(0, num_numbers):
    temp_password += random.choice(numbers)
for symbol in range(0, num_symbols):
    temp_password += random.choice(symbols)
print(temp_password)

random.shuffle(temp_password)
print(temp_password)

final_password = ""
for char in temp_password:
    final_password += char
print(f"Your password is: {final_password}")

# This code is a password generator that creates a random password based on user input for the number of letters, 
# symbols, and numbers. It first creates a list of letters, numbers, and symbols. Then it prompts the user to input
# how many of each they want in their password. It uses a for loop to add the specified number of random letters, 
# numbers, and symbols to a temporary password list. After that, it shuffles the temporary password list to ensure 
# randomness. Finally, it concatenates the characters in the temporary password list into a final password string 
# and prints it out to the user.