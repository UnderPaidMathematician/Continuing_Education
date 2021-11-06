from Resource import Resource
from Recipe import Recipe
import copy

class ResourceManager():
    # Initialize with our two dictionaries
    def __init__(self, ingredientList, recipeList) -> None:
        
        # build a list of resource objects that hold resource name and quantity
        self.availableResources = []
        for k,v in ingredientList.items():
            self.availableResources.append(Resource(k, v))
        
        # build a list of recipes
        self.recipes = []
        for a, b in recipeList.items():
            # builds recipe object with name and cost
            recipe = Recipe(a, b["cost"])
            # fills recipe object ingredient list with Resource Objects
            for c, d in b["ingredients"].items():
                recipe.Ingredients.append(Resource(c,d))
                self.recipes.append(recipe)

    def CreateProduct(self, recipe, customer, coinMachine):
        isResourcesAvailable = self.HasResourcesAvailable(recipe)
        isBalanceAvailable = customer.hasBalanceAvailable(recipe)
        if isResourcesAvailable == True and isBalanceAvailable == True:
            self.displayResourceLevels()
            print(f"Brewing {recipe.getName()}")
            # Remove balance from customers account for the item purchased 
            customer.changeBalance(-1*recipe.Product.Price)
            print(customer.getCustomerInfo())
            
            for recipeResource in recipe.Ingredients:
                getMatchingResource = Resource.GetByName(self.availableResources, recipeResource.Name)
                getMatchingResource.changeQuantity(-1*recipeResource.Quantity)

            self.displayResourceLevels()
            return True
        elif isResourcesAvailable == True and isBalanceAvailable == False:
            addedCoins = coinMachine.insertCoins()
            customer.changeBalance(addedCoins)
            return False
        elif isResourcesAvailable == False:
            print("Add more ingredients")
            return False

    def displayResourceLevels(self):
        for r in self.availableResources:
            print(f"{r.Name} has {r.Quantity} available.")        

    def getResourcesList(self):
        return copy.deepcopy(self.availableResources)

    def getRecipe(self, name):
        for r in self.recipes:
            if r.getName() == name:
                return copy.deepcopy(r)

    def getAllRecipes(self):
        return copy.deepcopy(self.recipes)

    def HasResourcesAvailable(self, recipe):
        isResourceAvailable = []
        for r in recipe.Ingredients:
            amountNeeded = r.getQuantity()
            amountAvailable = r.GetByName(self.availableResources, r.getName()).getQuantity()
            if amountNeeded <= amountAvailable:
                isResourceAvailable.append(True)
            else:
                isResourceAvailable.append(False)
        
        collectFalse =  [x for x in isResourceAvailable if x == False]

        if collectFalse == []:
            # this looks backwards but if there was no false then we have all resources available.
            return True
        else:
            return False
        
