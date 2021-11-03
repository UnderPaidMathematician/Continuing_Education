from Product import Product

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