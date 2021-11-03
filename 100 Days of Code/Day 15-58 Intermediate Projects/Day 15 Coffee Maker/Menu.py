from InitialData import MenuData

class Menu():
    def __init__(self) -> None:
        pass
    
    # There was a bit of confusion here as to why this worked without specifying self
    # Maybe its because I am dealing with just the imported MenuData
    # Note to self: Research this further
    def getCoffeeNames(self):
        coffeeNameList = [x for x in MenuData]
        return coffeeNameList

    def getRecipe(self, coffeeName):
        return MenuData[coffeeName]["ingredients"]

    
    def getCost(self, coffeeName):
        return MenuData[f"{coffeeName}"]["cost"]



