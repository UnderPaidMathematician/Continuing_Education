import tkinter
from tkinter import ttk

# Global
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Command Center
def startCommand():
    pass

def resetCommand():
    pass

def updateWorkTime(selection):
    workTimeValues = {"Not Motivated": 5, "Motivated": 10, "Highly Motivated": 20, "In the Zone": 30}
    workTime.set(workTimeValues[selection])

# Window
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)

# Canvas
canvas = tkinter.Canvas(width=200, height=223, background=YELLOW, highlightthickness=0)
tomatoImg = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 111.5, image=tomatoImg)
canvas.create_text(100, 111.5, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Timer Label
timerLabel = tkinter.Label(text="Timer", foreground=GREEN, font=(FONT_NAME, 35, "bold"), background=YELLOW)
timerLabel.grid(row=0, column=1)

# Dropdown for Rest Time
restLabel = tkinter.Label(text="Rest Time (min):", background=YELLOW)
restLabel.grid(row=5, column=1)
restTime = ttk.Combobox(window, values=[i for i in range(1, 31)], state="readonly")
restTime.grid(row=6, column=1)
restTime.set(SHORT_BREAK_MIN)  # Default value

# Dropdown for Work Time
workLabel = tkinter.Label(text="Work Time (min):", background=YELLOW)
workLabel.grid(row=7, column=1)
workTime = ttk.Combobox(window, values=[i for i in range(1, 61)], state="readonly")
workTime.grid(row=8, column=1)
workTime.set(WORK_MIN)  # Default value

# Radiobuttons for Motivation Levels
motivationLevels = ["Not Motivated", "Motivated", "Highly Motivated", "In the Zone"]
motivationVar = tkinter.StringVar(value=motivationLevels[0])  # Default to first option
for i, level in enumerate(motivationLevels):
    rb = tkinter.Radiobutton(window, text=level, variable=motivationVar, value=level, command=lambda lv=level: updateWorkTime(lv), background=YELLOW)
    rb.grid(row=9+i, column=1)

# Start and Reset Buttons
startButton = tkinter.Button(text="START", background='white', foreground='black', command=startCommand)
startButton.grid(row=2, column=0)

resetButton = tkinter.Button(text="RESET", background='white', foreground='black', command=resetCommand)
resetButton.grid(row=2, column=2)

window.mainloop()
