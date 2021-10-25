'''
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################
I removed the hints.

'''
# Interesting so this is a pretty bland blackjack game. Cards are not removed from the deck as they are drawn. o.O
# Challenge excepted!
def deck_builder():
    card_values = [[1,11], 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    card_labels = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    
    zipped_cards = zip(card_labels, card_values)
    dict_labels_w_values = dict(zipped_cards)

    print(dict_labels_w_values)
    '''
    deck = []
    for label in card_labels:
        for suit in suits:
            for value in card_values:
                deck["suit"] = {f'"{label}": {label}, "value": {value}, suit: {suit}'}
    return deck

'''
    
    
    





deck_1 = deck_builder()
print(deck_1)