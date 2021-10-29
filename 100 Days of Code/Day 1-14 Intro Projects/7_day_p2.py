# I am re using code for this challenge. I like mine better than the code used for the course. 
# This time they want us to build a interface with "_" for missing characters. 

'''
Modified instructions (I removed their code.)
#Step 2

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
'''

import random


#Step 1 

word_list = ["aardvark", "baboon", "camel"]

def GetNewWord(word_list):
    return word_list[random.randint(0, len(word_list)-1)]
    
new_word = GetNewWord(word_list)


# Todo 1: build a list of _ for each letter in the word.
placeholder_list = []
for i in new_word:
    placeholder_list.append("_")

player_guess = input("Guess a letter: \n").lower()


list_results = []

# added enumerate so I can get my index easily
# Todo 2: replace "_" with correct guess
for idx, chr in enumerate(new_word):
    if chr == player_guess:
        list_results.append(True)
        
        # overwrite "_" with character
        placeholder_list[idx] = player_guess

    else:
        list_results.append(False)

# Printed for testing purposes.
print(f"The word was: {new_word}")

# Print the results
print(placeholder_list)

