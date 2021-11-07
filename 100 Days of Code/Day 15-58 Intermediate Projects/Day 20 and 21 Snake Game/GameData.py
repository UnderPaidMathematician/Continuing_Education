# By building this class am I basically making my making my variables global? I.E. all parts of my program have access to it? Or is it the fact that it is contained within a class stop it from being truely global?

import re


class GameData():
    def __init__(self, heartBeatTime, screenHeight, screenWidth, goFasterModulus, score) -> None:
        # Determines the speed of the game
        self.GameHeartbeatTime = heartBeatTime

        # dimensions of the screen
        # Mixxed feelings here if I allow the user to scale the screen I have to scale the game to match. Not sure if I want to do this. 
        # I suppose if I make the game default 10x10 or something then scaling it could become easier. 
        self.ScreenHeight = screenHeight
        self.ScreenWidth = screenWidth

        # Level is the score for eating a frog 
        # Modulus is how many levels until the game speeds up.
        self.GoFasterModulus = goFasterModulus
        self.Score = score


    # Is this nessesary here? I feel like there is always one set of GameData no matter what. 
    def Copy(self):
        return GameData(heartBeatTime=self.GameHeartbeatTime, screenHeight=self.ScreenHeight, screenWidth=self.ScreenWidth,goFasterModulus=self.GoFasterModulus ,score=self.Score)

    def GetGameHeartbeatTime(self):
        return self.GameHeartbeatTime

    def GetGoFasterModulus(self):
        return self.GoFasterModulus

    def GetScreenHeight(self):
        return self.ScreenHeight
    
    def GetScreenWidth(self):
        return self.ScreenWidth


    




        