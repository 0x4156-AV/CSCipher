import sys, os
import Tkinter
from caesar import caesar
from Tkinter import *

app = Tkinter.Tk()
app.title("CSCipher")
app.geometry("650x500+200+200")

e = Entry(app, width=60, justify=CENTER).grid(row=1, column=1)

def callback():
    string = e.get()
    caesar(string)

b = Button(app, text="Start", width=10, command=callback).grid(row=1, column=2)

app.mainloop()
