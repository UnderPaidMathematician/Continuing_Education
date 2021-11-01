from InitialData import resources

class CurrentResources():
    def __init__(self) -> None:
        self.water = resources["water"]
        self.milk = resources["milk"]
        self.coffee = resources["coffee"]    

    def getWaterLevels(self):
        return self.water

    def getMilkLevels(self):
        return self.milk    

    def getCoffeeLevels(self):
        return self.coffee

    def getLevelsReport(self):
        return f"Water Level: {self.water}\nMilk Level: {self.milk}\nCoffee Level: {self.coffee}"

    # negative amounts subtract water positive amounts add water
    def changeWaterLevel(self, amount):
        self.water += amount
    
    def changeMilkLevel(self, amount):
        self.milk += amount

    def changeCoffeeLevel(self, amount):
        self.coffee += amount



