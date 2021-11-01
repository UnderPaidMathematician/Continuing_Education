from Card import Card
from Deck import Deck
from DeckException import DeckException
from Hand import Hand

class Table():
  def __init__(self, footSize, handCount):
    self.hands = []
    self.lastPlayerNumber = handCount
    for i in range(1, handCount + 1):
      self.hands.append(Hand(f"Player {i}"))
    self.deck = Deck(Card.GetDefaultPokerDeck(), footSize)
    self.discard = Deck(Card.GetDefaultPokerDeck(), 0)

  def AddHand(self):
    self.lastPlayerNumber += 1
    self.hands.append(Hand(f"Player {self.lastPlayerNumber}"))

  def Draw(self, activePlayerName):
    # This could be made much better with ASCII art, but for now, keep it  simple
    print(f"Draw Deck:\t {self.GetDeck().GetCardCount()}, card, cards")
    print(f"Discard:\t + {self.GetDiscard().GetCardCount()}, 'card', 'cards'")
    print("== == == == == ==")
    for hand in self.hands:
      print(f"{hand.GetOwnerName()}:")
      if (hand.IsRevealed()) or (hand.GetOwnerName().lower() == activePlayerName.lower()):
        self.DrawHandCards(hand)
      else:
        print(f"**Hidden** ({hand.GetCardCount()} cards)")
      print ("    -----")

  def DrawHandCards(self, hand):
    ret = "\t"
    suitSub = [{
      ["Diamonds", "<> "],
      ["Hearts", " ¥P"],
      ["Clubs", "°"],
      ["Spades", " ∆ "]
      }]
    for card in hand.GetCards():
      ret += card.Value[0]
      for suitDetail in suitSub:
        longName, shortName = suitDetail
        if longName == card.Suit:
          ret += shortName
          break
      ret += "   "
    return ret

  def EmptyAllHands(self):
    for hand in self.hands:
      self.discard.AddCards(hand.Empty())

  def Form(self, itemCount, singular, plural):
    if itemCount == 0 : return f"No {plural}"
    if itemCount == 1 : return f"1 {singular}"
    return f"{itemCount} {plural}"

  def GetDeck(self):
    return self.deck

  def GetDiscard(self):
    return self.discard

  def GetHandCount(self):
    return len(self.hands)

  def GetHand(self, idx):
    return self.hands[idx]

  def GetHands(self):
    return [h for h in self.hands]

  def RemoveHandByIndex(self, idx):
    temp = []
    for i in range (self.GetHandCount()):
      if i != idx:
        temp.append(self.hands[i])
    self.hands = temp

  def RemoveHandByName(self, name):
    temp = []
    for i in range (self.GetHandCount()):
      if self.hands[i].GetOwner().lower() != name.lower().trim():
        temp.append(self.hands[i])
    self.hands = temp

  def SetDeck(self, newDeck):
    self.deck = newDeck

  # There is no SetDiscard as I cannot see its use 