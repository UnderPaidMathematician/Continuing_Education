from turtle import Turtle, Screen
from random import choice

screen = Screen()

# Note my program adapts to different screen heights and widths
# Making the resolution too small would generate errors. 
# But the turtles are positioned on the starting line based on the height and width.
screenWidth = 500 
screenHeight = 400
screen.setup(width=screenWidth, height=screenHeight)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Hmm I have global variables here for position there most likely is a better way. Possibly a data class?
buffer = int(.05*screenHeight)
bufferedWidth = screenWidth -2*buffer
bufferedHeight = screenHeight -2*buffer
numberOfTurtles = len(colors)
turtleOffset = bufferedHeight/numberOfTurtles

turtleList = []
def turtleBuilder():
    for c in colors:
        newTurtle = Turtle(shape='turtle')
        newTurtle.speed('fastest')
        newTurtle.color(c)
        newTurtle.penup()
        turtleList.append(newTurtle)
    return turtleList

def turtlePositionStartingLine():
    startingLineXvalue = -bufferedWidth/2
    yPositionList = list(range(-int(bufferedHeight/2), int(bufferedHeight/2), int(turtleOffset)))
    
    for i, t in enumerate(turtleList):
        t.goto(x=startingLineXvalue, y=yPositionList[i] + turtleOffset/2)

def turtleRace():
    turtleMaxDistancePercentage = .15
    turtleMaxMove = int(turtleMaxDistancePercentage*screenWidth)
    turtleMaxWobbleAngle = 15
    percentBackwards = .2
    turtleMoveRange = list(range(-int(percentBackwards*turtleMaxMove), turtleMaxMove,1))
    turtleWobbleRange = list(range(-turtleMaxWobbleAngle, turtleMaxWobbleAngle, 1))

    isRaceFinished = False
    while isRaceFinished == False:
        for turtle in turtleList:
            move = choice(turtleMoveRange)
            wobble = choice(turtleWobbleRange)

            # If turtle goes past the top or bottom of screen force it to come back.
            if turtle.ycor() <= -bufferedHeight/2 + turtleOffset:
                wobble = turtleMaxWobbleAngle
            
            if turtle.ycor() >= bufferedHeight/2 - turtleOffset:
                wobble = -turtleMaxWobbleAngle
            
            turtle.left(wobble)

            # check for turtle moving forwards.
            if move == abs(move):
                for m in range(move):
                    turtle.fd(1)

                    if turtle.xcor() >= int(bufferedWidth/2):
                        # we have a winner
                        return turtle
            else:
                # move backwards
                for m in range(move, 0, 1):
                    turtle.fd(-1)
                    if turtle.xcor() >= int(screenWidth/2):
                        # we have a winner
                        return turtle

colorChoice = int(screen.numinput(title= "Who Will Win?", prompt="1=red 2=orange 3=yellow 4=green 5=blue 6=purple", minval=1, maxval=6))

userChoiceTurtle = Turtle()
userChoiceTurtle.color(colors[colorChoice-1])
userChoiceTurtle.hideturtle()

turtleList = turtleBuilder()

turtlePositionStartingLine()

winnerTurtle = turtleRace()

if userChoiceTurtle.color()[0] == winnerTurtle.color()[0]:
    screen.textinput(prompt=f"The winner is the {winnerTurtle.color()[0]} turtle!", title="You win!")
else:
    screen.textinput(prompt=f"The winner is the {winnerTurtle.color()[0]} turtle!, you chose {userChoiceTurtle.color()[0]}.", title=f"You lose!")

screen.exitonclick()