import sys, os
import Tkinter
from caesar import caesar
from Tkinter import *
import tkMessageBox

# Setup application interface
app = Tkinter.Tk()
app.title("CSCipher")
app.geometry("650x500+200+200")

# Create the funtions to call from the GUI
def callback():
    string = labelText.get()
    tkMessageBox.showinfo("Caesar Cipher finished",caesar(string))

def beenClicked():
    

# Make and put the buttons on a grid on the window
labelText = StringVar(None)
textEntry = Entry(app, width=57, justify=CENTER, textvariable=labelText).grid(row=1, column=1)
submitButton = Button(app, text="Start", width=10, command=callback).grid(row=1, column=2)
relStatus = StringVar().set(None)
radiobutton = RadioButton(app, text="", value="", variable=relStatus, command=beenClicked).grid(row=2, column=1)
radiobutton = RadioButton(app, text="", value="", variable=relStatus, command=beenClicked).grid(row=2, column=1)
radiobutton = RadioButton(app, text="", value="", variable=relStatus, command=beenClicked).grid(row=2, column=1)
radiobutton = RadioButton(app, text="", value="", variable=relStatus, command=beenClicked).grid(row=2, column=1)

# Start the application
app.mainloop()
