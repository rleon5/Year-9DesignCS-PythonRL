import tkinter as tk

from tkinter import *

from tkinter import messagebox


def submit(*args):
	print(textbox.size())
	print("Water Entry: ", waterEntry.get(), "Sleep: ", sleepEntry.get())
	#if textbox.size() > 0:
	#	textbox.delete(0,tk.END)
	if int(waterEntry.get()) < 2 and int(sleepEntry.get()) < 8:
		textbox.insert(tk.INSERT, "You need more water, and sleep")
	elif int(waterEntry.get()) < 2:
		textbox.insert(tk.INSERT, "You need more water")
	elif int(sleepEntry.get()) < 8:
		textbox.insert(tk.INSERT, "You need more sleep")

	


root = tk.Tk()
root.config(background = "grey")


root.geometry("400x400+0+900")

root.title("How Active Are You")


sleepLabel = tk.Label(root, text = "How much sleep did you get today in hours?")
sleepLabel.grid(row = 0, column = 1)
sleepEntry = tk.Entry(root)
sleepEntry.grid(row=1, column=1)


waterLabel = tk.Label(root, text = "How much water did you get today in litres?")
waterLabel.grid(row = 2, column = 1)


waterEntry = tk.Entry(root)
waterEntry.grid(row=3, column=1)
	

btn1 = tk.Button(root, text = "Submit Data", command = submit)
btn1.grid(row=5, column=1)


btn1.grid()


textbox = tk.Text(root, width = 20 , height = 10)
textbox.grid(row = 9, column = 0, columnspan = 2, sticky = "NESW", padx = 10)




root.mainloop()