import sys, os
import Tkinter
from caesar import caesar

app = Tkinter.Tk()
app.title("CSCipher")
app.geometry("650x500+200+200")

custName = stringVar(None) 
yourname = Entry(app, textvariable=custName).pack()

app.mainloop()

#flagFormat = input("How are flags formatted for this CTF? (ex. flag{}) ")
#string="wcrx{alczlj_trvjri}"
#caesar(string)
