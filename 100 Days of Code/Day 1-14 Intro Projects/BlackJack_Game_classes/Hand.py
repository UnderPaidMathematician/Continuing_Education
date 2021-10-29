from Card import Card
from DeckException import DeckException

class Hand():
  def __init__(self, ownerName):
    self.ownerName = ownerName.strip()
    self.isRevealed = False
    self.cards = []
    self.customData = None

  def Empty(self):
    ret = [c for c in self.cards]
    self.cards = []
    return ret

  def AddCard(self, card):
    self.cards.append(card)

  def AddCards(self, cardList):
    self.cards.extend(cardList)

  def GetCards(self):
    ret = [card for card in self.cards] # We don't want to return the original array - we want to return a copy of it
    return ret

  def GetCustomData(self):
    return self.customData

  def Hide(self):
    self.isRevealed = False

  def IsRevealed(self):
    return self.isRevealed

  def GetOwnerName(self):
    return self.ownerName

  def GetSize(self):
    return len(self.cards)

  def RemoveCard(self, card):
    idx = -1
    for i in range(self.GetSize()):
      possible = self.cards[i]
      if (possible.Suit == card.Suit) and (possible.Value == card.Value):
        idx = i
        break
    if idx == -1:
      raise DeckException("Card not in hand")

    temp = []
    for i in range(self.GetSize()):
      if i != idx:
        temp.append(self.cards[i])
    self.cards = temp

  def Reveal(self):
    self.isRevealed = True

  def SetCustomData(self, newData):
    self.customData = newData

  def SetOwnerName(self, ownerName):
    self.ownerName = ownerName.trim()