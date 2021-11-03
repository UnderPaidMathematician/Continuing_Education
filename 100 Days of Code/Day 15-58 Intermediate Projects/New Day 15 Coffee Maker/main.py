from InitialData import InitialData
from ResourceManager import ResourceManager


data = InitialData()
resourceManager = ResourceManager(data.INGREDIENTS, data.RECIPES)
resourceList = resourceManager.getResourcesList()
print(resourceList[0].getName())
print(resourceList[0].getQty())

recipeList = resourceManager.getRecipeList()
print(recipeList[0].getName())
print(recipeList[0].getIngredients()[0].getName())
print(recipeList[0].getIngredients()[0].getQty())
print(recipeList[0].getCost())
