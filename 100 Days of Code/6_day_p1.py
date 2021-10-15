'''
# I wrote code that needed to be done on a website.

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_around()


def jump(number_of_jumps):
    for j in range(number_of_jumps):
        move()
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()

jump(6)

# It worked first try with no edits. Not bad

'''