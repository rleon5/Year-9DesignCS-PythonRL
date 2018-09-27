import tkinter as tk
import math


# When you are dealing with event driven programming the program sits and waits for the user
# to do something. These are programs where you click a button and something happens. What we
# we do is BIND a function to a key.  So when we click the button the function runs. 
#
def submit():

	print("Submit pressed")

	r =float(entr.get())
	h =float(enth.get())

	v = math.pi*r*r*h
	v = round(v,3)

	output.config(state="normal")
	output.insert(tk.INSERT,v)
	output.config(state="disabled")

root = tk.Tk() 
root.title("Volume of a Cylinder")

labr = tk.Label(root, text="radius")
labr.pack()

entr = tk.Entry(root)
entr.pack()

labh = tk.Label(root, text="height")
labh.pack()

enth = tk.Entry(root)
enth.pack()

btn = tk.Button(root, text ="Submit", command = submit)
btn.pack()

output= tk.Text(root, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
output.config(state="disabled")
output.pack()




  
root.mainloop()
print("end program")