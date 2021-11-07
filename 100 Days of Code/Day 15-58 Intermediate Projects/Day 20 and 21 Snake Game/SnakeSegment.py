from turtle import Turtle

class SnakeSegment():
    def __init__(self) -> None:
        self.segment = Turtle(shape='arrow')
        self.segment.color(255,255,255)
        self.segment.penup()
    
    def Copy(self):
        return self.segment
    
    def TurnRight(self):
        self.segment.right(90)
    
    def TurnLeft(self):
        self.segment.left(90)


