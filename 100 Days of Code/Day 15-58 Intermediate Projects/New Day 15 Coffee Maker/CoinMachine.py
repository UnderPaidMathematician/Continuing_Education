from HelperFunctions import HelperFunctions

class CoinMachine():
    def __init__(self, customer) -> None:
        self.currentUser = customer
        self.coinValues = {"Quarter": .25, "Dime": .10, "Nickle": .05, "Penny": .01}
    
    def insertCoins(self):
        print("Insert number of coins: ")
        numQuarters = HelperFunctions.askInteger("Quarters: ")
        numDimes = HelperFunctions.askInteger("Dimes: ")
        numNickles = HelperFunctions.askInteger("Nickles: ")
        numPennies = HelperFunctions.askInteger("Pennies: ")
        sumOfCoins = numQuarters * self.coinValues["Quarter"] \
            + numDimes * self.coinValues["Dime"] \
            + numNickles * self.coinValues["Nickle"] \
            + numPennies * self.coinValues["Penny"]
        return sumOfCoins
    
    def increaseBalance(self, amount):
        self.currentUser.changeBalance(amount)
    
    def cashOutBalance(self):
        pass
