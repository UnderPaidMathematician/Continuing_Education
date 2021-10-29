from DeckException import DeckException
from EmptyDeckException import EmptyDeckException

from Card import Card
from Hand import Hand
from Table import Table
import os

class BlackJack():
    class Status():
        def __init__(self):
            self.HandState = "Active"
        #end Status class

    def __init__(self):
        self.table = Table(4, 3) #A foot of four decks, three players. For v1 we will just make these assumptions
        # The table also created a default poker deck, but it's not shuffled
        self.table.GetDeck().Shuffle()
        owners = ["Jason", "Draco", "House"]
        for i in range(len(owners)):
            hand = self.table.GetHand(i)
            hand.SetOwnerName(owners[i])
            hand.SetCustomData(self.Status())
            hand.Reveal() # everyone's hand will be revealed for now

    def ClearConsole(self):
        ## Clear code
        os.system('cls')

    def GetActivePlayers(self):
        ret = []
        for player in self.table.GetHands():
            if player.GetCustomData().Status == "Active":
                ret.append(player)
        return ret

    def GetStandingPlayers(self):
        ret = []
        for player in self.table.GetHands():
            if player.GetCustomData().Status == "Stand":
                ret.append(player)
        return ret

    def Run(self):
        numPlayers = self.table.GetHandCount()
        currentPlayer = 0
        totalGameCount = 1
        deckGameCount = 1
        recycleCount = 4
        table = self.table
        deck = table.GetDeck()

        true = True
        while(true): #endless loop:
            self.ClearConsole()
            table.Draw()
            print("===================")
            print("Players still active:")
            playerList = self.GetActivePlayers()
            if len(playerList) == 0:
                totalGameCount += 1
                deckGameCount += 1
                table.GetDiscard().AddCards(table.EmptyAllHands())
            if deckGameCount > recycleCount:
                deck.AddCards(table.GetDiscard().Empty())
                deckGameCount = 1
                deck.Shuffle()
                for hand in table.GetHands():
                    hand.AddCards(deck.DrawCards(2))
                    hand.GetCustomData().Status = "Active"
                    hand.Reveal()
                    currentPlayer = 0
            else:
                for p in playerList:
                    print(f"{p.GetOwnerName()}")
                    print("")
                    player = table.GetHand(currentPlayer)
                    print(f"Current player: {player.GetOwnerName()}")
                    isInputValid = False
                    
                while not isInputValid:
                    inp = input("Choose: Hit or Stand (enter H or S)").lower() # I added lower here
                    
                    # Not sure if this is needed anymore
                    # if len(inp) > 0:
                    #     switch(inp.lower())
                    
                    if inp == "s":
                        player.GetCustomData().Status = "Stand"

                    if len(self.GetActivePlayers) == 0:
                        standers = self.GetStandingPlayers()
                        highestPlayers = []

                        for stander in standers:
                            standerValue = self.ValueHand(stander)
                            if len(highestPlayers) == 0:
                                highestPlayers.append(stander)
                            elif standerValue < self.ValueHand(highestPlayers[0]):
                                pass # Not a winner
                            elif standerValue > self.ValueHand(highestPlayers[0]):
                                highestPlayers = [stander]
                            else: #Equal value

                                if stander.GetOwnerName() == "House":
                                    highestPlayers = [stander]
                                elif highestPlayers[0].GetOwnerName() == "House":
                                    pass # The house always wins
                                else:
                                    highestPlayers.append(stander)

                            print("The winners are:")
                            for hp in highestPlayers:
                                print(f"    {hp.GetOwnerName()}")
                                input ("Press Enter to go the next hand")
                                break
                    elif inp == "h":
                        player.AddCard(deck.DrawCard())
                        val = self.ValueHand(player)
                        if val > 21:
                            player.GetCustomData().Status = "Bust"

    def ValueHand(self, hand):
        total = 0
        aceCount = 0
        cards = hand.GetCards()

        for card in cards:
            if card.Value.isnumeric():
                total += int(card.Value)
            elif (card.Value[0].lower()) == "a":
                aceCount += 1
                break # These are calculated later
            elif (card.Value[0].lower()) == "j" or (card.Value[0].lower()) == "q" or(card.Value[0].lower()) == "k":
                total += 10
                break
            else:
                raise DeckException (f"Card value {card.Value} unknown.")

        #Now Aces
        for i in range(aceCount):
            if total + 11 < (21 - (aceCount - i)):
                total += 11
            else:
                total += 1

            return total 