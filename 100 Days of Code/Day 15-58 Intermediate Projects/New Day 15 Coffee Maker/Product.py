# This is a data class that is responsible for tracking product name and price
class Product():
    def __init__(self, name, price) -> None:
        self.Name = name
        self.Price = price
    
    def Copy(self):
        return(Product(self.Name, self.Price))