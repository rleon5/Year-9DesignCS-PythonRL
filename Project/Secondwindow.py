import tkinter as tk


root = Tk()


root.geometry("400x400+0+900")



root.title("How Active Are You")




sleepLabel = tk.Label(root, text = "how much sleep did you get today in hours")
sleepLabel.grid(row = 0, column = 1)
waterEntry = tk.Entry(root)
waterEntry.grid(row=1, column=1)

waterLabel = tk.Label(root, text = "how much water did you get today in litres")
waterLabel.grid(row = 2, column = 1)

waterEntry = tk.Entry(root)
waterEntry.grid(row=3, column=1)


submitButton = tk.Button(root, text="Submit", command= "submitData")
submitButton.grid(row=5, column=1)



root.mainloop()