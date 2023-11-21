import tkinter
from tkinter import ttk
import math
import pygame
import os
import sys

# Initialize Pygame Mixer
pygame.mixer.init()

# Global Variables
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"

# Constants for Time Intervals and Limits
MINIMIZE_DELAY = 5000  # Delay in milliseconds for auto minimize/maximize
MAX_SESSION_COUNT = 4  # Maximum number of work sessions before a long break
TIME_MULTIPLIER = 60  # Multiplier to convert minutes to seconds
UPDATE_INTERVAL = 1000  # Update interval for the countdown timer in milliseconds

# Global variables to track state and volume
sessionCount = 0
countDownTimer = None
isTimerActive = False
isWorkSession = True
shortBreakVolume = 0.5
longBreakVolume = 0.5

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def startCommand():
    global isTimerActive
    if not isTimerActive:
        isTimerActive = True
        startTimer()

def startTimer():
    global sessionCount, isWorkSession
    workTimeMinutes = int(workTime.get())
    if isWorkSession:
        if autoMinimizeVar.get():
            window.after(MINIMIZE_DELAY, lambda: window.iconify())
        countDown(workTimeMinutes * TIME_MULTIPLIER)
    else:
        if autoMinimizeVar.get():
            window.deiconify()
        if sessionCount < MAX_SESSION_COUNT:
            countDown(shortRestTime.get() * TIME_MULTIPLIER)
        else:
            countDown(longRestTime.get() * TIME_MULTIPLIER)

def startBreak(breakTime):
    global isTimerActive, isWorkSession
    isTimerActive = True
    countDown(int(breakTime) * TIME_MULTIPLIER)

    # Play sound based on the session count with volume control
    if sessionCount < MAX_SESSION_COUNT:
        shortBreakSound = pygame.mixer.Sound(resource_path('shortBreak.mp3'))
        shortBreakSound.set_volume(shortBreakVolume)
        shortBreakSound.play()
    else:
        longBreakSound = pygame.mixer.Sound(resource_path('longBreak.mp3'))
        longBreakSound.set_volume(longBreakVolume)
        longBreakSound.play()

def resetCommand():
    global isTimerActive, sessionCount, isWorkSession
    window.after_cancel(countDownTimer)
    canvas.itemconfig(timerText, text="00:00:00")
    sessionCount = 0
    checkMarkLabel.config(text="")
    isTimerActive = False
    isWorkSession = True
    updateTimerLabel()

def countDown(count):
    global countDownTimer, sessionCount, isWorkSession
    canvas.itemconfig(timerText, text=f"{math.floor(count/3600):02}:{math.floor(count/60 % 60):02}:{math.floor(count % 60):02}")

    if count > 0:
        countDownTimer = window.after(UPDATE_INTERVAL, countDown, count - 1)
    else:
        isTimerActive = False
        if isWorkSession:
            sessionCount += 1
            checkMarkLabel.config(text=(CHECK_MARK + "\n") * sessionCount)
            isWorkSession = False
            if sessionCount < MAX_SESSION_COUNT:
                startBreak(shortRestTime.get())
                window.deiconify()
            else:
                startBreak(longRestTime.get())
                window.deiconify()
                sessionCount = 0
        else:
            window.after(MINIMIZE_DELAY, lambda: window.iconify())
            isWorkSession = True
        updateTimerLabel()

def updateTimerLabel():
    if isWorkSession:
        timerLabel.config(text="Work", foreground=GREEN)
    else:
        timerLabel.config(text="Break", foreground=RED)

def setWorkTime(level):
    global isTimerActive, isWorkSession, countDownTimer
    selectedTime = int(motivationTimes[level].get())
    workTime.set(selectedTime)

    if isTimerActive:
        window.after_cancel(countDownTimer)
        isTimerActive = False

    isWorkSession = True
    startCommand()

def adjustShortBreakVolume(val):
    global shortBreakVolume
    shortBreakVolume = float(val)

def adjustLongBreakVolume(val):
    global longBreakVolume
    longBreakVolume = float(val)

# Window Setup
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)
autoMinimizeVar = tkinter.BooleanVar(value=True)
autoMinimizeCheckbutton = tkinter.Checkbutton(window, text="Auto Minimize/Maximize", var=autoMinimizeVar, background=YELLOW)
autoMinimizeCheckbutton.grid(row=16, column=1, columnspan=2)

# Canvas
canvas = tkinter.Canvas(width=200, height=223, background=YELLOW, highlightthickness=0)
tomatoImg = tkinter.PhotoImage(file=resource_path('tomato.png'))
canvas.create_image(100, 111.5, image=tomatoImg)
timerText = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1, columnspan=3)

# Timer Label
timerLabel = tkinter.Label(text="Timer", foreground=GREEN, font=(FONT_NAME, 35, "bold"), background=YELLOW)
timerLabel.grid(row=0, column=1, columnspan=3)

# Dropdowns for Rest Times and Work Time
shortRestLabel = tkinter.Label(text="Short Rest Time (min):", background=YELLOW)
shortRestLabel.grid(row=5, column=1)
shortRestTime = ttk.Combobox(window, values=[i for i in range(1, 481)], state="readonly", width=10)
shortRestTime.grid(row=6, column=1)
shortRestTime.set(SHORT_BREAK_MIN)

longRestLabel = tkinter.Label(text="Long Rest Time (min):", background=YELLOW)
longRestLabel.grid(row=5, column=2)
longRestTime = ttk.Combobox(window, values=[i for i in range(1, 481)], state="readonly", width=10)
longRestTime.grid(row=6, column=2)
longRestTime.set(LONG_BREAK_MIN)

workLabel = tkinter.Label(text="Work Time (min):", background=YELLOW)
workLabel.grid(row=7, column=1)
workTime = ttk.Combobox(window, values=[i for i in range(1, 481)], state="readonly", width=10)
workTime.grid(row=8, column=1)
workTime.set(WORK_MIN)

# Motivation Level Buttons and Dropdowns
motivationLevels = {
    "Not Motivated": 5,
    "Motivated": 10,
    "Highly Motivated": 25,
    "Flow Zone": 60
}
motivationTimes = {}
for i, (level, defaultTime) in enumerate(motivationLevels.items()):
    button = tkinter.Button(window, text=level, command=lambda lv=level: setWorkTime(lv), background=YELLOW)
    button.grid(row=12+i, column=1)

    motivationTime = ttk.Combobox(window, values=[i for i in range(1, 481)], state="readonly", width=10)
    motivationTime.grid(row=12+i, column=2)
    motivationTime.set(defaultTime)
    motivationTimes[level] = motivationTime

# Start and Reset Buttons
startButton = tkinter.Button(text="START", background='white', foreground='black', command=startCommand, highlightthickness=0)
startButton.grid(row=2, column=1)

resetButton = tkinter.Button(text="RESET", background='white', foreground='black', command=resetCommand, highlightthickness=0)
resetButton.grid(row=2, column=2)

# Check Mark Label
checkMarkLabel = tkinter.Label(text="", background=YELLOW, foreground=GREEN, font=(FONT_NAME, 15, "bold"))
checkMarkLabel.grid(row=1, column=3)

# Volume Controls for Break Sounds
shortBreakVolumeLabel = tkinter.Label(text="Short Break Volume:", background=YELLOW)
shortBreakVolumeLabel.grid(row=17, column=1)
shortBreakVolumeSlider = tkinter.Scale(window, from_=0, to=1, orient='horizontal', resolution=0.01, command=adjustShortBreakVolume)
shortBreakVolumeSlider.set(0.5)
shortBreakVolumeSlider.grid(row=18, column=1)

longBreakVolumeLabel = tkinter.Label(text="Long Break Volume:", background=YELLOW)
longBreakVolumeLabel.grid(row=17, column=2)
longBreakVolumeSlider = tkinter.Scale(window, from_=0, to=1, orient='horizontal', resolution=0.01, command=adjustLongBreakVolume)
longBreakVolumeSlider.set(0.5)
longBreakVolumeSlider.grid(row=18, column=2)

window.mainloop()
