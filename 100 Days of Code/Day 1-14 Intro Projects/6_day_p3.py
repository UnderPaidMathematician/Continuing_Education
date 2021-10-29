'''
# So far these have been really easy. But Its still pretty fun. Easy day today so far. 

https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_around()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while at_goal() == False:
    if wall_in_front():
        jump()
    else:
        move()
'''