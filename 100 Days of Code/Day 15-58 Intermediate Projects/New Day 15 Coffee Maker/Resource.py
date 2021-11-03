# Data Class 
# Name of the resource (water, milk, coffee)
# Initial starting quantity
class Resource():
    def __init__(self, name, quantity) -> None:
        self.Name = name
        self.Quantity = quantity
    
    def getName(self):
        return self.Name
    
    def getQuantity(self):
        return self.Quantity
    
    @staticmethod
    def GetByName(resourceList, name):
        for r in resourceList:
            if r.Name == name:
                return r
        return None