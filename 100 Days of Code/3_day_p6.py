print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to go fishing.") 

# I chose a function because I want to be able to return "Game Over" if they make a poor choice.
def day_at_the_lake():
    
    # Choice 1
    # Assume mistakes have been made
    incorrect_input = True
    choices_1 = ["right","left","l","r"]

    while incorrect_input:
        user_choice = input("On the left there is a beautiful lake on the right there is a highway. Choose to go left or right.\t").lower()
        for choice in choices_1:
            if user_choice == choices_1[0] or user_choice == choices_1[3]:
                print(f"You decide to enjoy the lake.")
                incorrect_input = False
                break
            elif user_choice == choices_1[1] or user_choice == choices_1[2]:
                print(f"You decide to drive and find another lake... You never find one. You lose.")
                return "Game Over"
            else:
                pass
                
    
    # Choice 2
    # Assume mistakes have been made
    incorrect_input = True
    choices_1 = ["walk", "swim","s","w"]

    while incorrect_input:
        user_choice = input("Swim or walk along the shore?\t").lower()
        for choice in choices_1:
            if user_choice == choices_1[0] or user_choice == choices_1[3]:
                print(f"You walk to find the perfect fishing spot.")
                incorrect_input = False
                break
            elif user_choice == choices_1[1] or user_choice == choices_1[2]:
                print(f"You try and swim but that scares away the fish! You lose.")
                return "Game Over"
            else:
                pass
                

    # Choice 3
    # Assume mistakes have been made
    incorrect_input = True
    # I was a little smarter about the order of the choices this time
    choices_1 = ["pool", "p", "rapids","tree","rock","r", "t"]

    while incorrect_input:
        user_choice = input("Where do you cast your line? (pool, rapids, tree, or rocks)?\t").lower()
        for choice in choices_1:
            if user_choice == choices_1[0] or user_choice == choices_1[1]:
                print(f"You catch a fish!!!")
                incorrect_input = False
                return "You Win!"
            elif user_choice == choices_1[2] or user_choice == choices_1[3] or user_choice == choices_1[4] or user_choice == choices_1[5]:
                print(f"You dont catch a fish!")
                return "Game Over"
            else:
                pass
                             

result = day_at_the_lake()
print(result)

