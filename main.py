import sys, os
import Tkinter
from caesar import caesar
from Tkinter import *

app = Tkinter.Tk()
app.title("CSCipher")
app.geometry("650x500+200+200")

e = Entry(app, width=100, wrap=WORD)
e.pack()
e.focus_set()

def callback():
    string = e.get()
    caesar(string)

b = Button(app, text="Start", width=10, command=callback)
b.pack()

app.mainloop()
