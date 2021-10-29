# I decided to try my hand and using classes for this project
# It was not something that was asked for but I felt it would be better

class Pizza():

    # I used static methods since small medium and large would always have these values. 
    
    @staticmethod
    class PizzaSizes():
        Small = "Small"
        Medium = "Medium"
        Large = "Large"


    
    # size = PizzaSizes().Small
    def __init__(self, size) -> None:
        self.size = size
    
    def GetName(self):
        return self.size + " Pizza"

