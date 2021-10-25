# This program will have two settings easy with 10 tries and hard with 5 tries
# Guess a number between 1 and 100
# Tell the user if they are correct, higher or lower than the answer.
# If they run out of guesses they lose. 
import random
from art_12 import art

def player_setup(): 
    invalid_input = True
    while invalid_input:
        player_difficulty = input("Choose a difficulty: Easy or Hard. ").lower()
        # Note they can type easy or e and it will work. 
        if player_difficulty[0] == 'e':
            player_lives = 10
            return player_lives
        elif player_difficulty[0] == 'h':
            player_lives = 5
            return player_lives
        else:
            print("invalid Input try again.")

def build_range(max):
    return [x for x in range(1, max+1)]
    
def player_guess():
    invalid_input = True
    while invalid_input:
        player_guess = input("Guess a whole number: ")
        if player_guess.isnumeric():
            invalid_input = False
            return int(player_guess)        

# Start
# Building my list of options.
list_of_options = build_range(100)

random.shuffle(list_of_options)

target_number = list_of_options[0]
print(art)
print(f"I am thinking of a number between {min(list_of_options)} and {max(list_of_options)}.")
player_lives = player_setup()

list_of_options = build_range(100)

random.shuffle(list_of_options)

target_number = list_of_options[0]

keep_playing_game = True
while keep_playing_game:

    p_guess = player_guess()
    player_lives -= 1

    if p_guess == target_number:
        print("You win!")
        keep_playing_game = False
    elif p_guess > target_number:
        print(f"Your guess was too high. Tries remaining {player_lives}")
    elif p_guess < target_number:
        print(f"Your guess was too low. Tries remaining {player_lives}")
    
    if player_lives < 1:
        print(f"Sorry the number was {target_number}, You lose.")
        keep_playing_game = False

    









