'''
I noticed a edge case where the robot would get stuck in a loop. 

I fixed it but later I watched the teacher do it and her solution was a little more elegant than mine. But our results were similar.
I basically recorded previous moves and then sliced my list to see when the last 4 vs the last 8:4 matched and then I forced the robot to take a different move. 

Her solution was to in the begining run the robot into a wall and then turn him before starting the normal function. The maze never changes I wonder if there would be a difference between ours if the maze was different.


def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_around()

turn_list = []
back_four = []
back_eight = []
while at_goal() == False:
    
    # Noticed an issue where there were edge cases where the robot gets stuck in a loop.
    if len(turn_list) >= 8:
    
        back_four = turn_list[-4:]
        back_eight = turn_list[-8:-4]
       
    if back_four == back_eight:
        print(back_four)
        print(back_eight)
        if front_is_clear():
            move()
        elif right_is_clear():
            turn_right()
        else:
            turn_left()
  
    if right_is_clear():
        turn_right()
        move()
        turn_list.append("right")
    elif front_is_clear():
        move()
        turn_list.append("straight")
    else:
        turn_left()
        turn_list.append("left")
    print(turn_list)
'''