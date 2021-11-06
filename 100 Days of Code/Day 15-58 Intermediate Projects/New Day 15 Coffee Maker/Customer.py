import copy

class Customer():
    def __init__(self, customerName, currentBalance) -> None:
        self.customerName = customerName
        self.currentBalance = currentBalance

    def getBalance(self):
        return self.currentBalance

    def getName(self):
        return copy.deepcopy(self.customerName)

    def hasBalanceAvailable(self, recipe):
        costOfCoffee = recipe.Product.Price
        if costOfCoffee <= self.currentBalance:
            return True
        else:
            print(f"You need to add more funds. {recipe.Name} costs ${recipe.Product.Price}")
            print(f"You only have a balance of {self.currentBalance}")
            return False
    
    def changeBalance(self, amount):
        self.currentBalance += amount

    def changeName(self, newName):
        self.customerName = newName

    def getCustomerInfo(self):
        print(f"Hello {self.getName()} your current balance is: ${self.getBalance():.0f}")

