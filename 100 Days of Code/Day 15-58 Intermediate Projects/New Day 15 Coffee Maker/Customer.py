class Customer():
    def __init__(self, name, balance) -> None:
        self.Name = name
        self.balance = balance

    def GetBalance(self):
        return self.balance

    def GetName(self):
        return self.Name

    def CanAfford(self, recipe):
        costOfCoffee = recipe.Product.Price
        if costOfCoffee <= self.balance:
            return True
        else:
            return False
    
    def AddBalance(self, amount):
        self.balance += amount

    def SubtractBalance(self, amount):
        self.balance -= amount

    def SetName(self, newName):
        self.Name = newName



