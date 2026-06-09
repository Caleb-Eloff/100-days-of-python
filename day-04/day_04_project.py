import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

options = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)
if player_choice > 3 or player_choice < 0:
    print("You typed an invalid number, you lose!")
    exit()
else:
    print("Player chose:" + options[player_choice])
    print("Computer chose:" + options[computer_choice])

if player_choice == computer_choice:
    print("It's a draw!")
elif (player_choice == 0 and computer_choice == 2) or \
     (player_choice == 1 and computer_choice == 0) or \
     (player_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose!")

# This code implements a simple Rock-Paper-Scissors game. The player is prompted to choose rock, paper, or scissors
# by entering 0, 1, or 2. The computer randomly selects its choice using the random module. The program then 
# compares the player's choice with the computer's choice and determines the outcome of the game (win, lose, or 
# draw) based on the standard rules of Rock-Paper-Scissors.
