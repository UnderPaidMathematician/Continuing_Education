# Higher Lower Game

from day_14_higher_lower_art import logo
from day_14_higher_lower_art import vs
from day_14_higher_lower_game_data import data
from os import system

from random import shuffle

def player_input():
    '''Checks to see if the player input is valid and returns it.'''
    notCorrect: bool = True
    while notCorrect:
        guess = input("Choose A or B: ").lower()
        if guess == 'a' or guess == 'b':
            return guess

# I cant tell if the items can repeat themselves so I am assuming that they dont.
# It will be easier to remove items from a list I also want to shuffle the items.
game_card_list = data

# Shuffle the list order
shuffle(game_card_list)



notGameOver = True
first_card_index = 0
second_card_index = 1
player_correct_count = 0
while notGameOver:
    # Clear the screen
    system('cls')

    print(logo)

    print(f"You currently have {player_correct_count} correct. \n")

    first_card = game_card_list[first_card_index]
    second_card = game_card_list[second_card_index]

    first_card_count = first_card["follower_count"]
    second_card_count = second_card["follower_count"]

    # Check and save the results
    winner = ''
    if first_card_count == second_card_count:
        winner = 's'
    elif first_card_count > second_card_count:
        winner = 'a'
    else:
        winner = 'b'


    print(f"Choose A: {first_card['name']}, {first_card['description']} from {first_card['country']}")
    print(vs)
    print(f"Choose B: {second_card['name']}, {second_card['description']} from {second_card['country']}")
    
    player_choice = player_input()

    # Checks for a tie (both a and b are correct)
    if winner == 's': 
        player_correct_count += 1
    # If the player is correct they keep going
    elif player_choice == winner:
        player_correct_count += 1
    else:
        notGameOver = False
        print(f"\nA: {first_card['name']}, {first_card['description']} from {first_card['country']} had {first_card['follower_count']} followers.")
        print(f"B: {second_card['name']}, {second_card['description']} from {second_card['country']} had {second_card['follower_count']} followers.\n")
        print(f"You lose! You got {player_correct_count} correct. Better luck next time.")

    # second card becomes A and second card is the next card in the list.
    first_card_index += 1
    second_card_index += 1  







