import tkinter as tk
import time

def minimize():
    root.iconify()

def maximize():
    root.deiconify()

root = tk.Tk()
root.geometry("300x200")

minimize_button = tk.Button(root, text="Minimize", command=minimize)
minimize_button.pack()

maximize_button = tk.Button(root, text="Maximize", command=maximize)
maximize_button.pack()

root.mainloop()
