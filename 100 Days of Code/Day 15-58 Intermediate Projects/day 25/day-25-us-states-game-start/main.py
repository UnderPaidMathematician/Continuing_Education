import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
imagePath = r"blank_states_img.gif"
screen.addshape(imagePath)
turtle.shape(imagePath)

stateLocationData = pd.read_csv("50_states.csv")
foundStates = []

isGameFinished = False
while isGameFinished != True:
    userGuess = screen.textinput(title=f"Guess the state {len(foundStates)}/50", prompt="Whats another states name?")
    x, y = None, None
    allStates = stateLocationData['state'].tolist()
    if userGuess.lower() == 'exit':
        statesToLearnList = []

        [statesToLearnList.append(state) for state in allStates if state.lower() not in foundStates]

        pd.DataFrame(data=statesToLearnList, columns=["learn these states"]).to_csv('statesToLearn.csv')
        break

    for state in allStates:
        if userGuess.lower() == state.lower():
            stateDataRow = stateLocationData[stateLocationData['state'] == state]

            turtleWriter = turtle.Turtle()
            turtleWriter.penup()
            turtleWriter.goto(int(stateDataRow['x']), int(stateDataRow['y']))
            turtleWriter.write(arg=state)

            if userGuess.lower() not in foundStates:
                foundStates.append(userGuess.lower())

    if len(foundStates) == 50:
        isGameFinished = True

