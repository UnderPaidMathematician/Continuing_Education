class Customer():
    def __init__(self, customerName, currentBalance) -> None:
        self.customerName = customerName
        self.currentBalance = currentBalance

    def getBalance(self):
        return self.currentBalance

    def getName(self):
        return self.customerName        
    
    def changeBalance(self, amount):
        self.currentBalance += amount

    def changeName(self, newName):
        self.customerName = newName

    def getCustomerInfo(self):
        return f"Hello {self.getName()} your current balance is: {self.getBalance()}"

