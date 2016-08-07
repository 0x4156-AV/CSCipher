import sys
import collections
import binascii
import base64
from string import ascii_lowercase
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename

def get_format():
    ask_format = input("What is the format of your flags? ").upper()
    accepted = "ABCDEFGHIJKLMNOPQRSTVWXYZ"
    global flag_format
    flag_format = ""
    for i in ask_format:
        if i in accepted:
            flag_format += i

def open_file():
    root = Tk()
    root.withdraw()
    name = askopenfilename(initialdir="~/Desktop",
                           filetypes =(("Text File", "*.txt"),("All Files","*.*")),
                           title = "Choose a file.")
    try:
        with open(name,'r') as UseFile:
            global ciphertext
            ciphertext = str(UseFile.read()).upper()

    except:
        print("No file exists")

def get_ciphertext():
    ask = input("What is the ciphertext? (Type 1 to choose a text file) ")
    if ask is "1":
        open_file()
    else:
        global ciphertext
        ciphertext = ask

def find_key(string):
    number = len(string)
    array = []

    dict = collections.defaultdict(int)
    for character in string:
        dict[character] += 1

    for character in ascii_lowercase:
        array.append((dict[character]/float(number)))

    num = array.index(max(array))
    key = (((num - 5) % 26) + 1)
    return key

def decrypt(n, ciphertext):
    key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result

def caesar(string):
    global flag_format
    key = str(find_key(string))
    decrypted = str(decrypt(find_key(string), string.upper()))
    if flag_format in decrypted or flag_format is decrypted:
        print("\033[1mKey Used:\033[0m " + str(key) + "\n\033[1mGot flag:\033[0m " + str(decrypted))
    else:
        for i in range(1,26):
            brute = str(decrypt(int(i), string.upper()))
            if flag_format in brute or flag_format is brute:
                print("\033[1mKey Used:\033[0m " + str(i) + "\n\033[1mGot flag:\033[0m " + str(brute))
                sys.exit(0)

def check_binary():
    global ciphertext
    binary_accepted = "10 "
    new_accepted = "10"
    if(all(c in binary_accepted for c in ciphertext)):
        # Remove formatting of the binary
        newciphertext = ""
        for i in ciphertext:
            if i in new_accepted:
                newciphertext += i
        n = int(str(newciphertext), 2)
        text = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
        print("\033[1mGot flag:\033[0m " + text)
        sys.exit(0)

def check_base16():
    global ciphertext
    global flag_format
    try:
        b16 = base64.b16decode(ciphertext).decode('ascii').upper()
        if flag_format in b16 or flag_format is b16:
            print("\033[1mGot flag:\033[0m " + b16)
            sys.exit(0)
    except binascii.Error:
        pass

def check_base32():
    global ciphertext
    global flag_format
    try:
        b32 = base64.b32decode(ciphertext).decode('ascii').upper()
        if flag_format in b32 or flag_format is b32:
            print("\033[1mGot flag:\033[0m " + b32)
            sys.exit(0)
    except binascii.Error:
        pass

def check_base64():
    global ciphertext
    global flag_format
    try:
        b64 = base64.b64decode(ciphertext).decode('ascii').upper()
        if flag_format in b64 or flag_format is b64:
            print("\033[1mGot flag:\033[0m " + b64)
            sys.exit(0)
        else:
            pass
    except UnicodeDecodeError:
        pass

def check_bases():
    check_base16()
    check_base32()
    check_base64()

def main():
    global ciphertext
    get_format()
    get_ciphertext()
    check_binary()
    check_bases()
    print("Finished preliminary tests, moving onto ciphers")
    caesar(ciphertext)

try:
    main()
except KeyboardInterrupt as a:
    print("\nGoodbye!")
except ImportError as b:
    print("\nYou must have Tkinter installed")
