from GuessResult import GuessResult
from Guess import Guess

gameModes = [["Easy", 10], ["Hard", 5]]

def CreateGuess(modeName):
  if (modeName == None) or (len(modeName) < 1):
    modeName = "e"

  modeLetter = modeName[0].lower()
  for modeType in gameModes:
    modeName, modeGuesses = modeType
    if (modeName[0].lower() == modeLetter):
      return Guess(100, modeGuesses)
  return None

guess = None
while guess == None:
  prompt = "====== Guessing Game ======\n"
  prompt += "Purpose: Guess a number from 1 to 100 in a set amount of tries. I will tell you each time if you got it right or were too high or low.\n"
  prompt += "Modes and Guesses allowed are:\n"
  for m in gameModes:
    modeName, modeGuesses = m
    prompt += f"\t{modeName}:\t{modeGuesses}\n"
  prompt += "Which mode would you like to play? (First letter) > "
  guess = CreateGuess(input(prompt))

triesRemaining = guess.GetRemainingTryCount()
isCorrect = False

while (isCorrect == False) and (guess.HasRemaining()):
  userGuess = ""
  while (len(userGuess) < 1) or (userGuess.isnumeric() == False):
    userGuess = input(f"Tries Remaining: {triesRemaining} \tYour guess? ")
  result = guess.TryNumber(userGuess)
  triesRemaining = result.AttemptsRemaining
  isCorrect = result.IsCorrect
  print (f"==== {result.Direction} ====")

if isCorrect:
  print ("You win!")
else:
  print (f"Out of guesses, sorry. The number was {guess.GetTarget()}") 