#import tkinter module so i can have a nice guifrom
from tkinter import *
#import messagebox(a module that displays nice alerts and more)
from tkinter import messagebox

# The function called when the submit button is pressed
def submitData():
	# a nice looking alert using messagebox from tkinter that displays the values from the entries
	messagebox.showinfo("Form Data has Been Submited", "Thank you for submiting: " + nameEntry.get() + ageEntry.get() + "!")



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