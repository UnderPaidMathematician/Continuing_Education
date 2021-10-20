# Objective is to build a rock paper scissors game

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# art choices appended to a list
list_choices = []
list_choices.extend([rock, paper, scissors])

# get the users input
player_choice = input("Choose Rock, Paper, or Scissors as (R, P, S).\t").lower()


# Choice list
choice_list = ["Rock", "Paper", "Scissors"]

# assume that the player chose something incorrect 
bad_choice = True
while bad_choice:
    for i, c in enumerate(choice_list):
        if player_choice == c[0].lower():
            bad_choice = False
            # I use this later in my matrix
            player_choice_index = i 
            break
        # if we got to the end of our list without a valid choice
        elif i == len(choice_list) - 1:
            print("invalid choice")
            player_choice = input("Choose Rock, Paper, or Scissors as (R, P, S).\t").lower()

# Possible results as a dictionary
results = {0:"Lose", 1:"Win", 2:"Draw"}

# Results based on computer choice outcomes rock, paper, scissors
# so based on the above dictionary values 
p_rock = [2, 0, 1]
p_paper = [1, 2, 0]
p_scissors = [0, 1, 2]

# making a list of lists
result_matrix = []
result_matrix.extend([p_rock, p_paper, p_scissors])

# computer makes its choice
computer_choice = random.randint(0,2)

# Results for player choice
print(f"You chose: {choice_list[player_choice_index]}")
print(list_choices[player_choice_index])

# Results for computer choice
print(f"The computer chose: {choice_list[computer_choice]}")
print(list_choices[computer_choice])

# Final outcome
print(f"You {results[(result_matrix[player_choice_index][computer_choice])]}!\n")










