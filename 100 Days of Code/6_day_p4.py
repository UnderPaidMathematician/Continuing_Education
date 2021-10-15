'''
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

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

def full_jump():
    turn_left()
    
    what_goes_up = 0
    while wall_on_right():
        move()
        what_goes_up += 1
        
    turn_right()
    move()
    turn_right()
    
    # Since what goes up must come down.
    for i in range(what_goes_up):
        move()
    turn_left()    

while at_goal() == False:
    if wall_in_front():
        full_jump()
    else:
        move()
'''