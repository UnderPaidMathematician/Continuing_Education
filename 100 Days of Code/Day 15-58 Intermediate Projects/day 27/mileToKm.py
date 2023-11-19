import tkinter

globalXPad = 5
globalYPad = 5
windowHeight = 200
windowWidth = 300

window = tkinter.Tk()
window.config()
window.title("Miles to Km Converter")
window.geometry(f"{windowWidth}x{windowHeight}")



# definitions
def convertMileToKm():
    try:
        userInput = float(inputBox.get())
        result = userInput * 1.609344
        resultLabel.config(text=f"{result}")
        errorLabel.config(text="")
        window.update()
    except ValueError:
        errorLabel.config(text="Numbers Only")


# labels
errorLabel = tkinter.Label(text="", padx=globalXPad, pady=globalYPad)
errorLabel.grid(row=0, column=0)

mileLabel = tkinter.Label(text="Miles", padx=globalXPad, pady=globalYPad)
mileLabel.grid(row=0, column=2)

kmLabel = tkinter.Label(text="Km", padx=globalXPad, pady=globalYPad)
kmLabel.grid(row=1, column=2)

isEqualToLabel = tkinter.Label(text="Is equal to:", padx=globalXPad, pady=globalYPad)
isEqualToLabel.grid(row=1, column=0)

resultLabel = tkinter.Label(text="", padx=globalXPad, pady=globalYPad)
resultLabel.grid(row=1, column=1)

# Input box
inputBox = tkinter.Entry(0, justify='center')
inputBox.grid(row=0, column=1)

# button
calculateButton = tkinter.Button(text="Calculate", command=convertMileToKm)
calculateButton.grid(row= 2, column=1)


window.mainloop()
