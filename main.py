from checkflag import *
from ciphers.bases import *
from ciphers.caesar import Caesar
message = "MFRGG"
flagFormat = checkFlag()
caesar = Caesar()
bases = Bases()
print(caesar.caesar(message))
print(bases.base16(message))
print(bases.base32(message))
print(bases.base64(message))
