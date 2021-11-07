from SnakeSegment import SnakeSegment

class SnakeBuilder():
    def __init__(self) -> None:
        self.SnakeSegmentList = []

    def buildNewSegment(self):
        if self.SnakeSegmentList == []:
            # Build the head of the snake
            self.SnakeSegmentList.append(SnakeSegment().Copy())
        else:
            # make a copy of the tail
            print(self.SnakeSegmentList[-1])
            self.SnakeSegmentList.append(self.SnakeSegmentList[-1].clone())
            self.SnakeSegmentList[-1].fd(-20)
    
    def GetSnakeSegmentList(self):
        return self.SnakeSegmentList