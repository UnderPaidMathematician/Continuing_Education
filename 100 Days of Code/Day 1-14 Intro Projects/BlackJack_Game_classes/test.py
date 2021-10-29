from Deck import Deck
from Card import Card

card1 = Card("Ace", "Spades")
card2 = Card("Jack", "Spades")
card3 = Card("Queen", "Spades")
card4 = Card("King", "Spades")
card5 = Card("10", "Hearts")

cardStack = [card1, card2, card3, card4]

deck = Deck(cardStack, 1)

card = deck.DrawCard()
print (f" {card.Value} of {card.Suit}") #Should be King of Spades since we didn't

deck.AddCard(card5)

ret = deck.GetCards()

ret = deck.GetCards.RandomShuffle()

for obj in ret:
    print(f'{obj.Value} of {obj.Suit}')





