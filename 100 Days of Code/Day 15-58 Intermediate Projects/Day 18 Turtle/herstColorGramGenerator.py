from turtle import Turtle, Screen
import turtle
import colorgram
from random import choice

# Change colormode to tuple of 255
dotPainter = Turtle()
turtle.colormode(255)
dotPainter.speed('fastest')
dotPainter.width(1)

# generate random colors from an image
extractedColors = colorgram.extract('100 Days of Code\Day 15-58 Intermediate Projects\Day 18 Turtle\SpotPainting04.jpg', 30)
print(extractedColors)

def chooseRandomColor():
    return choice(extractedColors)

def makeDot():
        currentColor = chooseRandomColor()
        dotPainter.color(currentColor.rgb)
        dotPainter.fillcolor(currentColor.rgb)
        dotPainter.stamp()

def moveForwardNoPen(gap):
    dotPainter.penup()
    dotPainter.fd(gap)
    dotPainter.pendown()

def drawDots(numberWide, gap):
    for r in range(numberWide):
        for c in range(numberWide):
            # if row is even draw forward make dot before moving
            # if row is odd draw backward made dot after moving
            if r % 2 == 0:
                makeDot()
                moveForwardNoPen(gap)
            else:
                moveForwardNoPen(-1*gap)
                makeDot() 

        # Move to next row
        dotPainter.left(90)
        moveForwardNoPen(-1*gap)
        dotPainter.right(90)


# I could have used dot instead but I ended up using stamp instead.
dotPainter.shape('circle')
dotPainter.shapesize(.5,.5,.5)

drawDots(10,50)

# hide the turtle when finished
dotPainter.hideturtle()

screen = Screen()
screen.exitonclick()
