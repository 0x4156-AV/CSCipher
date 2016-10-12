from checkflag import *
from ciphers.bases import *
from ciphers.caesar import Caesar
message = "MFRGG"
flagFormat = checkFlag()
caesar = Caesar()
bases = Bases()
check(caesar.caesar(message))
check(bases.base16(message))
check(bases.base32(message))
check(bases.base64(message))
