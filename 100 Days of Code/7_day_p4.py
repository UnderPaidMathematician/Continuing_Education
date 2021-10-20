# I am re using code for this challenge. I like mine better than the code used for the course. 
# This time they want us to build a interface with "_" for missing characters. 

'''
Modified instructions (I removed their code.)
Now we punish the player for guessing wrong. 
We also add visualizations for hangman to give user feedback.
Note my code is different then theirs but I like mine better. 
Theirs adds a bit of complexity when it comes to player lives and so forth. 
Mine checks for empty lists to keep track of player progress.
'''

import random

# I decided to clear the console upon creating a new game
import os

# Assuming windows clear the console for every game.
os.system('cls')


# Game Setup phase
word_list = ["aardvark", "baboon", "camel"]

def GetNewWord(word_list):
    return word_list[random.randint(0, len(word_list)-1)]
    
new_word = GetNewWord(word_list)

placeholder_list = []
for i in new_word:
    placeholder_list.append("_")

# adding hangman art 

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Game loop phase

gameOver = False

while not gameOver:
        
    player_guess = input("Guess a letter: \n").lower()

    # The results for the players guess
    list_results = []

    # Check to see if player made a good guess.
    # assume player guessed wrong 
    player_wrong_guess = True

    # added enumerate so I can get my index easily
    # Todo 2: replace "_" with correct guess
    for idx, chr in enumerate(new_word):
        if chr == player_guess:
            player_wrong_guess = False
            list_results.append(True)
            # overwrite "_" with character
            placeholder_list[idx] = player_guess

        else:
            list_results.append(False)
    
    # If the player guessed wrong display feedback
    if player_wrong_guess == True:
        current_feedback = stages.pop()
        print(f"Sorry {player_guess} was not correct.")
        print(current_feedback)

    # Printed for testing purposes.
    # print(f"The word was: {new_word}")

    # Print the results
    # Expanded my results to show better onscreen.
    friendly_result = ""
    for i in placeholder_list:
        friendly_result += i
        friendly_result += " "

    print(friendly_result)

    # Check for completed word
    # Builds an array of "_" for every "_" that is left over.
    listGameOver = [x for x in placeholder_list if x == "_"]

    if listGameOver == []:
        # If there are no blanks then the game is over.
        gameOver = True
        print("You win! Game over.")      
    # If there are no more stages the player has made too many wrong guesses.
    elif stages == []:
        gameOver = True
        print("You ran out of guesses. You lose!")
    else:
        print(f"Keep guessing you have {len(listGameOver)} letters left.\n")

