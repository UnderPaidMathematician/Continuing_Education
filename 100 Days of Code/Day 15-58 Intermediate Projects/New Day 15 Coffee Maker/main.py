from InitialData import InitialData
from ResourceManager import ResourceManager
from Customer import Customer
from HelperFunctions import HelperFunctions


def displayResourceLevels(resourceList):
    for r in resourceList:
        print(f"{r.Name} has {r.Quantity} available.")        


# Building my Data class
data = InitialData()

# Building a resource manager and passing it my two dictionaries
resourceManager = ResourceManager(data.INGREDIENTS, data.RECIPES)

# Uses the Initial Ingredients to put the coffee machine at its initial values for water, milk and coffee 
resourceList = resourceManager.getResourcesList()

allRecipes = resourceManager.getAllRecipes()

for currentRecipe in allRecipes:
    recipe = resourceManager.getRecipe(currentRecipe.getName())

customer = Customer("Jason", 0)

isProductFinished = False
while isProductFinished == False:
    coffeeMade = resourceManager.CreateProduct(recipe, customer)
    if coffeeMade == True:
        isProductFinished = True

