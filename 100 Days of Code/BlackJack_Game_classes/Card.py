#This is a data class. As such its members will be accessed directly, without getters/setters

class Card():
  def __init__(self, value, suit):
    self.Value = value
    self.Suit = suit

  @staticmethod
  def GetDefaultPokerList():
      suits = ["Diamonds", "Spades", " Hearts", "Clubs"]
      values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
      return [suits, values]

  @staticmethod
  def GetDefaultPokerDeck(hasJokers = False):
    suits, values = Card.GetDefaultPokerList()
    ret = []
    for suit in suits:
      for val in values: #value might be a reserved word so I use val instead
        ret.append(Card(val, suit))
    if hasJokers:
      ret.append(Card("Joker", "Big"))
      ret.append(Card("Joker", "Small"))
      return ret