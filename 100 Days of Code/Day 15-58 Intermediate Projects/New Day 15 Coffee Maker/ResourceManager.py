from Resource import Resource
from Recipe import Recipe

class ResourceManager():
    # Initialize with our two dictionaries
    def __init__(self, ingredientList, recipeList) -> None:
        
        # build a list of resource objects that hold resource name and quantity
        self.coffeeMachineResources = []
        for k,v in ingredientList.items():
            self.coffeeMachineResources.append(Resource(k, v))
        
        # build a list of recipes
        self.recipes = []
        for a, b in recipeList.items():
            # builds recipe object with name and cost
            recipe = Recipe(a, b["cost"])
            # fills recipe object ingredient list with Resource Objects
            for c, d in b["ingredients"].items():
                recipe.Ingredients.append(Resource(c,d))
                self.recipes.append(recipe)
    
    def getResourcesList(self):
        return self.coffeeMachineResources

    def getRecipe(self, name):
        for r in self.recipes:
            if r.getName() == name:
                return r
    
    def changeResourceQuantity(self, name, amount):
        self.Quantity += amount

    def HasResourcesAvailable(self, recipe):
        isResourceAvailable = []
        for r in recipe.Ingredients:
            amountNeeded = r.getQuantity()
            amountAvailable = r.GetByName(self.coffeeMachineResources, r.getName()).getQuantity()
            if amountNeeded <= amountAvailable:
                isResourceAvailable.append(True)
            else:
                isResourceAvailable.append(False)
        return isResourceAvailable

    def getAllRecipes(self):
        return self.recipes
    
    def CreateProduct(self, recipe):
        pass

