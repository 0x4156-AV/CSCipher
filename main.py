from checkflag import *
from ciphers.bases import *
from ciphers.caesar import Caesar
message = "MZWGCZ33NBUX2"
flagFormat = checkFlag()
caesar = Caesar()
bases = Bases()
caesar.caesar(message)
flagFormat.check_array(caesar.get_results())
flagFormat.check(bases.base16(message))
flagFormat.check(bases.base32(message))
flagFormat.check(bases.base64(message))
