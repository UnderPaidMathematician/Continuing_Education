class PizzaSize():
    @staticmethod
    def GetByName(pizzaSizes, name):
        for i in range(len(pizzaSizes)):
            if pizzaSizes[i].GetName() == name:
                return pizzaSizes[i]
            # except "Name " + name + " not found in GetByName of PizzaSize"

    @staticmethod
    def GetByIndex(pizzaSizes, idx):
        for i in range(len(pizzaSizes)):
            if pizzaSizes[i].GetIndex() == idx:
                return pizzaSizes[i]
    # except "Index  " + idx + " not found in GetByIndex of PizzaSize"

    def __init__(self, name, idx): #in many languages index is a reserved word so I use idx as 'index'
        self.name = name
        self.idx = idx

# self not defined
    def GetName():
        return self.name

    def GetIndex():
        return self.idx