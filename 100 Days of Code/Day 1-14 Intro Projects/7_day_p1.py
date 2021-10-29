import random


#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

def GetNewWord(word_list):
    return word_list[random.randint(0, len(word_list)-1)]

new_word = GetNewWord(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

player_guess = input("Guess a letter: \n").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

list_results = []

for chr in new_word:
    if chr == player_guess:
        list_results.append(True)
    else:
        list_results.append(False)

print(new_word)
print(list_results)