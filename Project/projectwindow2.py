import tkinter as tk

from tkinter import *

from tkinter import messagebox

def submitData():

	messagebox.showinfo("Form Data has Been Submited", "Thank you for submiting: " + nameEntry.get() + ageEntry.get() + "!")
	userName = waterEntry.get() + sleepEntry.get()
	print("Submit pressed")

root = tk.Tk()

root.geometry("400x400+0+900")

root.title("How Active Are You")

sleepLabel = tk.Label(root, text = "How much sleep did you get today in hours?")
sleepLabel.grid(row = 0, column = 1)
waterEntry = tk.Entry(root)
waterEntry.grid(row=1, column=1)

waterLabel = tk.Label(root, text = "How much water did you get today in litres?")
waterLabel.grid(row = 2, column = 1)

waterEntry = tk.Entry(root)
waterEntry.grid(row=3, column=1)

def onclick(args):

	if args == 1:
		print("Submitted")
submitButton = tk.Button(root, text = "Submit", command =lambda:onclick(1))
submitButton.grid(row=5, column=1)

def num():
print ("num in sleepLabel")


root.mainloop()