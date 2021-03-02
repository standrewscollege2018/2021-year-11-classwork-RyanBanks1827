from tkinter import *
# Creating the root obj
root=Tk()
# Set title of the window
root.title("First GUI")
# Set if window is resizable
root.resizable(width=FALSE, height=FALSE)
# Sets size of the window.
root.geometry("500x500")
# makes sure the darn window doesn't close
Label1= Label(root, text="Hi!", fg="#FF0000", bg="#FF3172")
Label1.pack(side=LEFT)
root.mainloop()