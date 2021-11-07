from turtle import Screen
from GameData import GameData
from SnakeBuilder import SnakeBuilder
from GameTimer import GameTimer

gameData = GameData(heartBeatTime = 1.0, screenHeight = 600, screenWidth = 600, goFasterModulus = 5, score = 0)
screen = Screen()
screen.setup(height = gameData.GetScreenHeight(), width = gameData.GetScreenWidth())
screen.colormode(255)
screen.bgcolor(0,0,0)

# TODO Create a Snake Body
snakeBuilder = SnakeBuilder()
for i in range(3):
    snakeBuilder.buildNewSegment()

# TODO Build Snake Movement

gameTimer = GameTimer(gameData=gameData)

isTime = False
while not isTime:
    screen.listen()
    if gameTimer.GetEllapsedTime() >= gameData.GetGameHeartbeatTime():
        for i in snakeBuilder.GetSnakeSegmentList():
            i.fd(20)
        isTime = True

# TODO Control the snake
# TODO Detect collision with food
# TODO Create a scoreboard
# TODO Detect collision with wall
# TODO Detect collision with tail

screen.exitonclick()