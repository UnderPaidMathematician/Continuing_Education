from Card import Card
from DeckException import DeckException
from EmptyDeckException import EmptyDeckException
import random

class Deck():
  def __init__(self, deckTemplate, footCount):
    #I don't know how to do so but I'd usually make sure right here that deckTemplate is an array of Card objects and raise an exception if it is not. This is called type-checking
    self.deckTemplate = deckTemplate
    self.footCount = footCount
    Reset()

  #This function is intended to be used to add a taken card back to the deck 
  def AddCard(self, card):
    self.deck.append(card)

  #As above but multiple cards at once
  def AddCards(self, cardList):
    self.deck.extend(cardList)

  # We are considering the last card in the array to be on top to minimize memory juggling
  def DrawCard(self)
    lastIndex = len(self.deck) - 1
    if lastIndex == -1
      raise EmptyDeckException("Cannot draw a card as the deck is empty.")
    ret = self.deck[lastIndex]
    self.deck.remove (lastIndex) #or however you remove the last item from the deck
    return ret

def DrawCards(self, howMany):
  ret = []
  drawCount = min(howMany, len(self.deck)) #Min function is supported, yes?
  for i in range(1, drawCount)
    ret.append(DrawCard())
  return ret

  def GetCards(self)
    ret = []
    for i in range(GetSize, 0) #This will count backwards, yes?
      ret.append(this.deck[i]) #Adding backwards since we consider the last card in this.deck to be on top
    return ret

  def GetSize(self)
    return len(self.deck)

  def Reset(self)
    self.deck = []
    for i in range (self.footCount)
      self.deck.extend(self.deckTemplate)

  def Shuffle(self)
    #The easy way is to create a new object and randomly choose from the existing list, pop a card and push it to the new list. However, the memory shuffling it causes is intense, so with a few more lines of code we can make this much more efficient:
    newDeck = [] #Still create a list to hold the new objects
    isTaken = [] #But also we will create a bit mask (true/false) for which cards are 'taken' so we don't have to pop anything...
    deckSize = len(self.deck)
    remaining = deckSize

    for i in range(deckSize)
      isTaken[i] = false

    while (remaining > 0)
      whichCard = random.randint(0, remaining - 1)
      found = 0
      currentIndex = 0
      while found <= whichCard
        if isTaken[current index]
           currentIndex += 1
        else
          if found == whichCard
            newDeck.append(self.deck[currentIndex])
            isTaken[currentIndex] = true
            remaining -= 1
          currentIndex += 1
          found += 1

      self.deck = newDeck 