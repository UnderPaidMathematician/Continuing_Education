from Recipe import Recipe
class RecipeManager():
    def __init__(self, recipeList) -> None:
        self.recipes = []
        for k, v in recipeList.items():
            self.recipes.append(Recipe(k,v["ingredients"], v["cost"]))

    def getRecipeList(self):
        return self.recipes