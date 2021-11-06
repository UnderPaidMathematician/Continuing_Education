# Data Class 
# Name of the resource (water, milk, coffee)
# Initial starting quantity
class Resource():
    def __init__(self, name, quantity) -> None:
        self.Name = name
        self.Quantity = quantity
    
    def Copy(self):
        return Resource(self.Name, self.Quantity)

    
    def GetName(self):
        return self.Name
    
    def GetQuantity(self):
        return self.Quantity
    
    def ChangeQuantity(self, amount):
        self.Quantity += amount
    
    @staticmethod
    def GetByName(resourceList, name):
        for r in resourceList:
            if r.Name == name:
                return r
        return None