from Product import Product

# Recipe data class
# Name is the name of the coffee
# Ingredients a list that will be filled in later
# Product that keeps track of name and price
class Recipe():
    def __init__(self, name, price) -> None:
        self.Name = name
        self.Ingredients = []
        self.Product = Product(name, price)
    
    def getName(self):
        return self.Name
    
    def getIngredients(self):
        return self.Ingredients
    
    def getCost(self):
        return self.Product.Price