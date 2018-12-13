#import tkinter module so i can have a nice guifrom
from tkinter import *
#import messagebox(a module that displays nice alerts and more)
from tkinter import messagebox

def submit(*args):
	global textbox
	global waterEntry
	global sleepEntry


	textbox.delete('1.0', END)

	print(textbox.size())
	print("Water Entry: ", waterEntry.get(), "Sleep: ", sleepEntry.get())
	#if textbox.size() > 0:
	#	textbox.delete(0,tk.END)
	if int(waterEntry.get()) < 2 and int(sleepEntry.get()) < 8:
		textbox.insert(INSERT, "You need more water, and sleep")
	elif int(waterEntry.get()) < 2:
		textbox.insert(INSERT, "You need more water")
	elif int(sleepEntry.get()) < 8:
		textbox.insert(INSERT, "You need more sleep")
	elif int(sleepEntry.get()) >= 8 and int(waterEntry.get()) >= 2:
		textbox.insert(INSERT, "You are in good condition")

# The function called when the submit button is pressed
def submitData():
	global textbox
	global waterEntry
	global sleepEntry
	# a nice looking alert using messagebox from tkinter that displays the values from the entries
	messagebox.showinfo("Form Data has Been Submited", "Thank you for submiting: " + nameEntry.get() + ageEntry.get() + "!")
	userName = nameEntry.get() + ageEntry.get()

	window2 = Tk()
	window2.geometry("400x400+0+900")
	window2.title("How Active Are You")

	sleepLabel = Label(window2, text = "How much sleep did you get today in hours?")
	sleepLabel.grid(row = 0, column = 1)
	sleepEntry = Entry(window2)
	sleepEntry.grid(row=1, column=1)

	waterLabel = Label(window2, text = "How much water did you get today in litres?")
	waterLabel.grid(row = 2, column = 1)

	waterEntry = Entry(window2)
	waterEntry.grid(row=3, column=1)	

	btn1 = Button(window2, text = "Submit Data", command = submit)
	btn1.grid(row=5, column=1)

	textbox = Text(window2, width = 20 , height = 10)
	#textbox.grid(row = 9, column = 3, columnspan = 2, sticky = "NESW", padx = 10)
	textbox.place(x=150, y=200)
	window2.mainloop()

	print(ageEntry.get())
	print(nameEntry.get())
	f = open("data.txt", "w")
	f.write(ageEntry.get())
	f.write(nameEntry.get())



#Vaiables 
userName = ""

#make the window
root = Tk()
# set the size/position, 33x400 for size, and 0,900 for x and y coordinates
root.geometry("400x400+0+900")
# The text you see on the bar at the top of the window
root.title("My Project")

# creates a label(text)
formLabel = Label(root, text="Fill out this form before so you can use the app")
# positions the label
formLabel.grid(row=0, column=2)

ageLabel = Label(root, text="What is your age?")
ageLabel.grid(row=2, column=1)

# creates the entry(where you enter the info)
ageEntry = Entry(root)
# positions it
ageEntry.grid(row=3, column=1)

nameLabel = Label(root, text="What is your name?")
nameLabel.grid(row=5, column=1)

nameEntry = Entry(root)
nameEntry.grid(row=6, column=1)

# creates a button, and when it's pressed it calls the function submitData
submitButton = Button(root, text="Submit", command=submitData)
submitButton.grid(row=8, column=1)



#keeps the window running instead of closing after 1 millisecond
mainloop()