import checkflag
from ciphers.caesar import Caesar
from ciphers.bases import *
message = "MFRGG"
flagFormat = checkflag()
caesar = Caesar()
bases = Bases()
print(caesar.caesar(message))
print(bases.base16(message))
print(bases.base32(message))
print(bases.base64(message))
