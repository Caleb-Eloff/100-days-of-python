import random

logo = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       '''

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
stages.reverse()

word_list = ["aardvark", "baboon", "camel"]

lives = 6

print(logo)

chosen_word = random.choice(word_list)

placeholder = ""
placeholder = "_" * len(chosen_word)
print(f"Word to guess: {placeholder}")

game_over = False
correct_guesses = []

while not game_over:

    print(f"******************{lives}/6 LIVES LEFT ******************")
    guess = input("Guess a letter: ").lower()   

    if guess in correct_guesses:
        print(f"You've already guessed {guess}.")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_guesses.append(letter)
        elif letter in correct_guesses:
            display += letter
        else:
            display += "_"
    
    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print("You lose! The word was: " + chosen_word)    

            print("*******************GAME OVER******************")

    if "_" not in display:
        game_over = True
        print("********************YOU WIN******************")

    print(stages[lives]) 
    
    
    