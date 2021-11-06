from turtle import Turtle, Screen
from random import randint, choice
import turtle

# This allows me to pass a tuple into pencolor to change the colors.
turtle.colormode(255)

tim = Turtle()
tim.shape('turtle')
tim.color('green')

def drawSquare():
    for i in range(4):
        tim.forward(100)
        tim.right(90)

def drawDottedLine(repeat, size):
    for _ in range(repeat):
        tim.pendown()
        tim.forward(size)
        tim.penup()
        tim.forward(size)

# I did this before she mentioned it. 
def randomColorPen():
    randomColor = (randint(0,255), randint(0,255), randint(0,255))
    tim.pencolor(randomColor)

def drawShapes(distance):
    shapeSideGenerator = list(range(3,11))
    for side in shapeSideGenerator:
        randomColorPen()
        angles = 360/side
        for _ in range(side):
            tim.right(angles)
            tim.fd(distance)

# Mine can take any angle not just 90 degrees.
def drawRandomWalk(angle, numberOfItterations, distance, width):
    tim.speed('fastest')
    tim.width(width)
    # builds a list of choices based on the chosen angle.
    angleChoices = list(range(0,360,angle))
    print(angleChoices)
    for _ in range(numberOfItterations):
        randomColorPen()
        tim.right(choice(angleChoices))
        tim.fd(distance)

# I decided to make mine with a hole in it. 
# I found it to be slightly more interesting. 
# I made hers first.
def drawSpirograph(angleTurn, holeDistance):
    tim.speed('fastest')
    numberOfRotations = list(range(0,360, angleTurn))
    print(numberOfRotations)
    for _ in numberOfRotations:
        randomColorPen()
        tim.left(angleTurn)
        tim.penup()
        tim.fd(holeDistance)
        tim.pendown()
        tim.circle(100)
        tim.penup()
        tim.right(180)
        tim.fd(holeDistance)
        tim.right(180)
        tim.pendown()
    

# Uncomment the one you want to see!
# drawSquare()

# drawDottedLine(10, 5)

# drawShapes(100)

# drawRandomWalk(90, 100, 50, 5)

drawSpirograph(5,100)

screen = Screen()
screen.exitonclick()
