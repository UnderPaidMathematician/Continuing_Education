from CoffeeMaker import CoffeeMaker
from CoinMachine import CoinMachine
from HelperFunctions import HelperFunctions

'''
 Goals:

1 Print report. Tell us how many resources are left.
2 when making coffee check to see if we have enough resources to complete the transaction
3 process coins that the user gave us for coffee
4 was the transaction successful? 
Check to see if they gave us enough money (we will need to make change for the customer)
5 make coffee. Removes resources from coffee maker. 
'''

# Code testing section            
testCoffeeMaker = CoffeeMaker()
# if testCoffeeMaker.loggedInCustomer == None:

testCoffeeMaker.displayUserLoginMenu()

curentUser = testCoffeeMaker.getLogedInUser()

testCoinMachine = CoinMachine(curentUser)
testCoinMachine.increaseBalance(testCoinMachine.insertCoins())
print(f"{testCoinMachine.currentUser.getName()} your balance is: {testCoinMachine.currentUser.getBalance():.2f}")

coffeeNameList = testCoffeeMaker.coffeeMakerMenu.getCoffeeNames()

for name in coffeeNameList:
    print(name)
    print(testCoffeeMaker.coffeeMakerMenu.getRecipe(coffeeName=name))
    print(testCoffeeMaker.coffeeMakerMenu.getCost(coffeeName=name))
