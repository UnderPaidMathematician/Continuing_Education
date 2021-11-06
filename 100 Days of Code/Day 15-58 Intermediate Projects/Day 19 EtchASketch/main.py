from turtle import Turtle, Screen

penObject = Turtle()
penObject.color('green')
penObject.speed('fastest')
screenObject = Screen()

def moveForward():
    penObject.fd(moveDistance)

def moveBack():
    penObject.fd(-moveDistance)

def rotateLeft():
    penObject.left(rotationAngle)

def rotateRight():
    penObject.right(rotationAngle)

def clearScreen():
    penObject.home()
    penObject.clear()

moveDistance = 10
rotationAngle = 10
# Program in dvorak so these key strokes look a bit strange. Translation WSAD C
screenObject.onkey(fun=moveForward, key=",")
screenObject.onkey(fun=moveBack, key="o")
screenObject.onkey(fun=rotateLeft, key="a")
screenObject.onkey(fun=rotateRight, key="e")
screenObject.onkey(fun=clearScreen, key='j')
screenObject.listen()

screenObject.exitonclick()

