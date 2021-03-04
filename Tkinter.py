def helloworld():
    print("Hello World")


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
hellobtn=Button(root, text="Say hello", command=helloworld)
stufflist=["Hi", "Bye", "Coolio"]
selectedstuff=StringVar()
selectedstuff.set(stufflist[0])
selectedstuff=OptionMenu(mainWindow, selectedstuff, stufflist)
selectedstuff.pack()
hellobtn.pack()

Label1.pack(side=LEFT)
root.mainloop()