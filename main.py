import sys, os, Tkinter
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
    determineMethod()

def beenClicked():
    cipherType = relStatus.get()

def determineMethod():
    if cipherType is "Caesar":
        tkMessageBox.showinfo("Caesar Cipher finished",caesar(string))
    elif cipherType is "Vigenere":
        tkMessageBox.showinfo("Vigenere","Vigenere")
    elif cipherType is "Baconian":
        tkMessageBox.showinfo("Baconian","Baconian")
    elif cipherType is "Affine":
        tkMessageBox.showinfo("Affine","Affine")
    elif cipherType is "ROT 13":
        tkMessageBox.showinfo("ROT 13","ROT 13")
    elif cipherType is "Binary":
        tkMessageBox.showinfo("Binary","Binary")
    elif cipherType is "Atbash":
        tkMessageBox.showinfo("Atbash","Atbash")
    elif cipherType is "Base 64":
        tkMessageBox.showinfo("Base 64","Base 64")
    elif cipherType is "Morse":
        tkMessageBox.showinfo("Morse","Morse")
    elif cipherType is "Auto":
        tkMessageBox.showinfo("Auto","Auto")
    else:
        tkMessageBox.showinfo("You broke it and idk how","You broke it and idk how")
# Make and put the buttons on a grid on the window
# Start with the textBox and Submit Button
labelText = StringVar(None)
textEntry = Entry(app, width=57, justify=CENTER, textvariable=labelText).grid(row=1, columnspan=4)
submitButton = Button(app, text="Start", width=10, command=callback).grid(row=1, column=4)

# Then put down the options for what cipher to use
relStatus = StringVar()
radiobutton = Radiobutton(app, text="Caesar", value="Caesar", variable=relStatus, command=beenClicked).grid(row=2, column=0)
radiobutton = Radiobutton(app, text="Vigenere", value="Vigenere", variable=relStatus, command=beenClicked).grid(row=2, column=1)
radiobutton = Radiobutton(app, text="Baconian", value="Baconian", variable=relStatus, command=beenClicked).grid(row=2, column=2)
radiobutton = Radiobutton(app, text="Affine", value="Affine", variable=relStatus, command=beenClicked).grid(row=2, column=3)
radiobutton = Radiobutton(app, text="ROT13", value="ROT13", variable=relStatus, command=beenClicked).grid(row=2, column=4)

radiobutton = Radiobutton(app, text="Binary", value="Binary", variable=relStatus, command=beenClicked).grid(row=3, column=0)
radiobutton = Radiobutton(app, text="Atbash", value="Atbash", variable=relStatus, command=beenClicked).grid(row=3, column=1)
radiobutton = Radiobutton(app, text="Base 64", value="Base 64", variable=relStatus, command=beenClicked).grid(row=3, column=2)
radiobutton = Radiobutton(app, text="Morse", value="Morse", variable=relStatus, command=beenClicked).grid(row=3, column=3)
radiobutton = Radiobutton(app, text="Auto", value="Auto", variable=relStatus, command=beenClicked).grid(row=3, column=4)

# Start the application
app.mainloop()
