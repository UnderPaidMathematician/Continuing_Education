class Resource():
    def __init__(self, name, qty) -> None:
        self.Name = name
        self.Qty = qty
    
    def getName(self):
        return self.Name
    
    def getQty(self):
        return self.Qty