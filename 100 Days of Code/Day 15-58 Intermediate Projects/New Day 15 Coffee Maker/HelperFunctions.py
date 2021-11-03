import os
import re

class HelperFunctions():
    @staticmethod
    def askIntegerRange(question, minimum, maximum):
        '''Input a string and get back a integer response within a specific range endpoints max and min included.'''
        badInput = True
        while badInput:
            userResponceInt = input(f"{question}: between {minimum} and {maximum}. ")
            if userResponceInt.isnumeric():
                userResponceInt = int(userResponceInt)
                if userResponceInt >= minimum and userResponceInt <= maximum:
                    return userResponceInt
            else:
                print("Invalid Input")

    @staticmethod
    def askInteger(question):
        '''Input a string and get back a integer response within a specific range endpoints max and min included.'''
        badInput = True
        while badInput:
            userResponceInt = input(f"{question}")
            if userResponceInt.isnumeric():
                userResponceInt = int(userResponceInt)
                badInput = False
                return userResponceInt
            else:
                print("Invalid Input")    

    @staticmethod
    def askYesOrNo(question):
        '''Input a string and get back a yes or no response.'''
        badInput = True
        while badInput:
            yesNo = input(f"{question}: ").lower()
            if yesNo[0] == 'y' or yesNo[0] == 'n':
                badInput = False
                return yesNo[0]
            else:
                print("Please answer Yes or No.")
    
    @staticmethod
    def clear_screen():
        '''Clears the console. Takes no arguments.'''
        os.system('cls')

    @staticmethod
    def writeAllPythonFilestoConsole():
        '''Gets all of the files that are marked as .py in a folder then appends them together into one file and writes it to console.'''
        os.system('cls')

        # Get all of the filepaths in a specific folder.
        directory = r'100 Days of Code\Day 15-58 Intermediate Projects\New Day 15 Coffee Maker'
        listOfPaths = []
        for filename in os.listdir(directory):
            if filename.endswith(".py"):
                listOfPaths.append(os.path.join(directory, filename))
            else:
                continue
        
        fullText = ""
        
        for currentPath in listOfPaths:
            with open(currentPath, 'r') as f:
                data = f.read()
            
            fullText += "---- " + currentPath.split("\\")[-1] + " ----\n\n" + data

        oldTextsize = len(fullText)
        isDone = False
        while not isDone:
            # fullText = re.sub('\n{2,}', '\n\n', fullText)
            fullText = re.sub("\n\s*\n(?:\s*\n)*", "\n\n", fullText)
            newTextSize = len(fullText)
            if oldTextsize == newTextSize:
                isDone = True
            else:
                oldTextsize = newTextSize

        print(fullText)



            

                
        