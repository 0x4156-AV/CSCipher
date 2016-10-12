from checkflag import *
from ciphers.bases import *
from ciphers.caesar import Caesar
message = "MFRGG"
flagFormat = checkFlag()
caesar = Caesar()
bases = Bases()
flagFormat.check(caesar.caesar(message))
flagFormat.check(bases.base16(message))
flagFormat.check(bases.base32(message))
flagFormat.check(bases.base64(message))
