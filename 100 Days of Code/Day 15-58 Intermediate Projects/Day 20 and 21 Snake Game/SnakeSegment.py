from turtle import Turtle

class SnakeSegment():
    def __init__(self) -> None:
        self.segment = Turtle(shape='arrow')
        self.segment.color(255,255,255)
        self.segment.penup()
    
    def Copy(self):
        copiedSegment = SnakeSegment()
        print(copiedSegment.segment.pos())
        copiedSegment.segment.pos = self.segment.pos
        print(copiedSegment.segment.pos())
        copiedSegment.segment.heading = self.segment.heading
        return copiedSegment

    def GetSegment(self):
        return self.segment




