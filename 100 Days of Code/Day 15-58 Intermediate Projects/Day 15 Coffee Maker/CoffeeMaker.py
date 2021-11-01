from Menu import Menu
from CurrentResources import CurrentResources
from Customer import Customer
from HelperFunctions import HelperFunctions

class CoffeeMaker():
    def __init__(self):
        self.coffeeMakerMenu = Menu
        self.coffeeMakerResources = CurrentResources
        self.userList = []
        self.loggedInUser = None
    
    def makeNewUser(self):
        badUserName = True
        while badUserName:
            # I am only ensuring that the name is not blank
            # I am also casting this as a string
            self.userNameInput = str(input("Please enter your name: "))
            if self.userNameInput == '':
                print("You must enter your name.")
            else:
                badUserName = False
        
        # customer starts with a zero balance in account
        self.userBalanceInput = 0

        currentUser = Customer(self.userNameInput, self.userBalanceInput)
        self.userList.append(currentUser)
    
    def getUserList(self):
        return self.userList

    def setLoginUser(self, userId):
        '''Sets the user login based on the ID that the user inputs.'''
        # fix userId since the user will enter one higher than the index of our list.
        userId = userId - 1
        userList = self.getUserList()
        self.loggedInUser = userList[userId]
    
    def getLogedInUser(self):
        """Returns the currently logged in user"""
        return self.loggedInUser

    def getUserNames(self):
        return [user.getName() for user in self.userList]

    def displayUserLoginMenu(self):
        # Clear the screen
        HelperFunctions.clear_screen()

        # If there are no users make one
        if self.userList == []:
            print("Hello and welcome Please make a new user.")
            self.makeNewUser()
        
        # Ask if they want to add another user
        addMoreUsers = True
        while addMoreUsers:
            custResponse = HelperFunctions.askYesOrNo("Would you like to add another user?")
            if custResponse == "y":
                self.makeNewUser()
            elif custResponse == "n" and len(self.getUserNames()) == 1:
                # if they did not add a user and there is only one user log them in
                self.setLoginUser(1)
                addMoreUsers = False
            elif custResponse == "n":
                addMoreUsers = False
        
        # Ask the user to login
        if self.loggedInUser == None:
            currentUsers = self.getUserNames()
            print("Please login: Choose from the following.")
            for i, v in enumerate(currentUsers):
                print(f"{i+1}: {v}")
            custResponse = HelperFunctions.askIntegerRange("Please enter the number of the person who wants to login.", minimum= 1, maximum= i+1)
            self.setLoginUser(custResponse)

    def logOutUser(self):
        '''Loggs out current customer.'''
        print("Thank you, customer has logged off.")
        self.loggedInUser = None
    
    def displayUserCoffeeChoiceMenu(self):
        '''Displays coffee options for users. Shows either prices or refill options.'''
        HelperFunctions.clear_screen()
        print(f"Hello {self.loggedInUser} You have a balance of {self.loggedInUser.getBalance()}what would you like to do?")



    







    