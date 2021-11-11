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

# for testing purposes
testColorList = ["red","yellow","green"]
for i, v in enumerate(testColorList):
    segmentList = snakeBuilder.GetSnakeSegmentList()
    segmentList[i].GetSegment().color(v)

# TODO Build Snake Movement

gameTimer = GameTimer(gameData=gameData)

isTime = False
while not isTime:
    screen.listen()
    screen.onkey(key='Right', fun=snakeBuilder.TurnRight)
    screen.onkey(key='Left', fun=snakeBuilder.TurnLeft)
    if gameTimer.GetEllapsedTime() >= gameData.GetGameHeartbeatTime():
        for i in snakeBuilder.GetSnakeSegmentList():
            print(i)
            print(i.GetSegment().pos())
            print(i.GetSegment().heading())
            i.GetSegment().fd(20)
        
        # Move Backwards through the snake.

        # print([x.GetSegment().heading() for x in snakeBuilder.GetSnakeSegmentList()])
        for i in range(len(snakeBuilder.GetSnakeSegmentList())-1, 0,  -1):
            # print(snakeBuilder.GetSnakeSegmentList()[i].GetSegment().heading())
            # print(snakeBuilder.GetSnakeSegmentList()[i-1].GetSegment().heading())
            if snakeBuilder.GetSnakeSegmentList()[i].GetSegment().heading() != snakeBuilder.GetSnakeSegmentList()[i-1].GetSegment().heading():
                snakeBuilder.GetSnakeSegmentList()[i].GetSegment().setheading(snakeBuilder.GetSnakeSegmentList()[i-1].GetSegment().heading())
        # print([x.GetSegment().heading() for x in snakeBuilder.GetSnakeSegmentList()])
        # isTime = True

# TODO Control the snake
# TODO Detect collision with food
# TODO Create a scoreboard
# TODO Detect collision with wall
# TODO Detect collision with tail

screen.exitonclick()