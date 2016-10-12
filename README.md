# CSCipher
A program that can determine and solve the type of encryption used on a string of encoded text.
This was created with Capture The Flag competitions in mind and solves algoithms mainly used there, not modern ciphers.
This program will be written entirely in Python and will later be transformed into Bash to be included in [aaronstoolkit](www.github.com/Aaronvigal.com/aaronstoolkit).
Created by [Aaron Vigal] (www.aaronvigal.com) on Saturday, July 23rd, 2016 for Millard West High School.

### The types supported by this program are:
----------------------------------------
* Affine
* Atbash
* Baconian✅
* Base 64/32/16 ✅
* Binary ✅
* Caesarian Shift ✅
* Morse Code ✅
* ROT13 ✅
* Vigenére Cipher ✅

CSCipher uses Pyhton 2.7 **not** Python 3.5 so if you don't already have that installed, install that from [here] (https://www.python.org/downloads/). To install the required dependencies and start up the application, execute the following commands in your terminal:
```bash
git clone -b master https://github.com/AaronVigal/CSCipher.git
cd CSCipher
python3 main.py
```
