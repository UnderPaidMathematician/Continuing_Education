from Resource import Resource
from Recipe import Recipe

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

    def CreateProduct(self, recipe, coinMachine):
        isResourcesAvailable = self.HasResourcesAvailable(recipe)
        
        if isResourcesAvailable == True:
            self.displayResourceLevels()
            # Remove balance from customers account for the item purchased 
            customer.changeBalance(-1*recipe.Product.Price)
            print(customer.getCustomerInfo())
            isBalanceAvailable = customer.hasBalanceAvailable(recipe)
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


    def getResourcesList(self):
        return [r.Copy() for r in self.availableResources]
        
    def getRecipe(self, name):
        for r in self.recipes:
            if r.getName() == name:
                return r
    
    def GetRecipe(self, name):
        for r in self.recipes:
            if r.getName() == name:
                return r.Copy()        

    def GetRecipeList(self):
        return [r.Copy() for r in self.recipes]

    def HasResourcesAvailable(self, recipe):
        isResourceAvailable = []
        for r in recipe.Ingredients:
            amountNeeded = r.getQuantity()
            amountAvailable = r.GetByName(self.availableResources, r.getName()).getQuantity()
            if amountNeeded <= amountAvailable:
                return True
            else:
                return False
    
    def GetMissingResources(self):
        missingResource = []
        for r in recipe.Ingredients:
            amountNeeded = r.getQuantity()
            amountAvailable = r.GetByName(self.availableResources, r.getName()).getQuantity()
            if amountNeeded >= amountAvailable:
                return True
                   
        
