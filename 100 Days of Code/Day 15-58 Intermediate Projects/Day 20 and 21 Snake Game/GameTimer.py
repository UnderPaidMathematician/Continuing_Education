import time

class GameTimer():
    def __init__(self, gameData) -> None:
        self.gameData = gameData
        self.start = time.time()        
    
    def GetEllapsedTime(self):
        timeNow = time.time()
        return timeNow - self.start
    



