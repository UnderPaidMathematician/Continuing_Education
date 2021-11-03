from InitialData import InitialData
from ResourceManager import ResourceManager

# Building my Data class
data = InitialData()

# Building a resource manager and passing it my two dictionaries
resourceManager = ResourceManager(data.INGREDIENTS, data.RECIPES)

# Uses the Initial Ingredients to put the coffee machine at its initial values for water, milk and coffee 
resourceList = resourceManager.getResourcesList()

recipe = resourceManager.getRecipe("cappuccino")

isResourcesAvailable = resourceManager.HasResourcesAvailable(recipe)

print(isResourcesAvailable)