# Import all my crap
from checkflag import *
from ciphers.bases import *
from ciphers.caesar import *
from ciphers.morse import *
from ciphers.baconain import *
from ciphers.vigenere import *
message = ""
# Setup all Classes
flagFormat = checkFlag()
caesar = Caesar()
bases = Bases()
morse = Morse()
baconain = Baconain()
vigenere = Vigenere()
# Run decryption functions
caesar.caesar(message)
flagFormat.check_array(caesar.get_results())
flagFormat.check(bases.base16(message))
flagFormat.check(bases.base32(message))
flagFormat.check(bases.base64(message))
flagFormat.check(morse.morse(message))
flagFormat.check(baconain.baconain(message))
flagFormat.check(vigenere.vigenere(message))
# Viaola!
