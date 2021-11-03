from Resource import Resource
from Recipe import Recipe

class ResourceManager():
    def __init__(self, ingredientList, recipeList) -> None:
        self.resources = []
        for k,v in ingredientList.items():
            self.resources.append(Resource(k, v))
        
        self.recipes = []
        for a, b in recipeList.items():
            recipe = Recipe(a, b["cost"])
            for c, d in b["ingredients"].items():
                recipe.Ingredients.append(Resource(c,d))
                self.recipes.append(recipe)

    
    def getResourcesList(self):
        return self.resources

    
    def getRecipeList(self):
        return self.recipes

