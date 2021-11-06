# Data Class 
# Name of the resource (water, milk, coffee)
# Initial starting quantity
class Resource():
    def __init__(self, name, quantity) -> None:
        self.Name = name
        self.Quantity = quantity
    
    def Copy(self):
        return Resource(self.Name, self.Quantity)

    
    def getName(self):
        return self.Name
    
    def getQuantity(self):
        return self.Quantity
    
    def changeQuantity(self, amount):
        self.Quantity += amount
    
    @staticmethod
    def GetByName(resourceList, name):
        for r in resourceList:
            if r.Name == name:
                return r
        return None