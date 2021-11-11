from SnakeSegment import SnakeSegment

class SnakeBuilder():
    def __init__(self) -> None:
        self.SnakeSegmentList = []
        self.PriorHeadingList = []

    def buildNewSegment(self):
        if self.SnakeSegmentList == []:
            # Build the head of the snake
            self.SnakeSegmentList.append(SnakeSegment())
        else:
            # make a copy of the tail
            # print(self.SnakeSegmentList[-1])
            self.SnakeSegmentList.append(self.SnakeSegmentList[-1].Copy())
            self.SnakeSegmentList[-1].GetSegment().fd(-20)
            print(self.SnakeSegmentList[-1].GetSegment().pos())
    
    def GetSnakeSegmentList(self):
        return self.SnakeSegmentList
    
    def TurnRight(self):
        self.SnakeSegmentList[0].GetSegment().setheading(self.SnakeSegmentList[0].GetSegment().heading() - 90)
    
    def TurnLeft(self):
        self.SnakeSegmentList[0].GetSegment().setheading(self.SnakeSegmentList[0].GetSegment().heading() + 90)    