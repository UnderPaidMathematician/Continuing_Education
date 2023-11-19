import tkinter

window = tkinter.Tk()
window.title("My first gui in python.")
window.minsize()
window.config(padx=20, pady=20)
myLabel = tkinter.Label(text="I am a label", font=("Arial", 24, "italic"))
myLabel.grid(column=0, row=0)
myLabel.config(text="New Text")


def buttonClicked():
    myLabel.config(text=input.get())

myButton = tkinter.Button(text="click me", command=buttonClicked)
myButton.grid(column=1, row=1)

newButton = tkinter.Button(text="New Button", command=buttonClicked)
newButton.grid(column=2, row=0)

input = tkinter.Entry(width=10)
input.grid(column=3, row=2)

window.mainloop()
