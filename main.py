import sys, os
import Tkinter
from caesar import caesar
from Tkinter import *

app = Tkinter.Tk()
app.title("CSCipher")
app.geometry("650x500+200+200")

e = Entry(app)
e.pack()
e.focus_set()

def callback():
    print e.get()

b = Button(app, text="Start", width=10, command=callback)
b.pack()

app.mainloop()

#flagFormat = input("How are flags formatted for this CTF? (ex. flag{}) ")
#string="wcrx{alczlj_trvjri}"
#caesar(string)
