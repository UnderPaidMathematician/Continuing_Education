from GuessResult import GuessResult
import random

class Guess():
  def __init__(self, maximumNumber, numberGuesses):
    self.target = random.randint(1, maximumNumber + 1)
    self.guessesRemaining = numberGuesses

  def GetRemainingTryCount(self):
    return self.guessesRemaining

  def GetTarget(self):
    return self.target

  def HasRemaining(self):
    if (self.guessesRemaining > 0):
      return True
    return False

  def TryNumber(self, num):
    if (self.guessesRemaining < 1):
      raise Exception("No guesses remain")
    if (num.isnumeric() == False):
      raise TypeError(f"TryNumber: {num} is not numeric") #Or whatever one fits

    num = int(num)
    
    if (num == self.target):
      return GuessResult ("Perfect!", True, self.guessesRemaining)
    self.guessesRemaining -= 1
    if (num < self.target):
      return GuessResult("Higher", False, self.guessesRemaining)
    return GuessResult ("Lower", False, self.guessesRemaining)
