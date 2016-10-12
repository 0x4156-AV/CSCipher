import base64
import binascii
class Bases:
    b16 = None;
    b32 = None;
    b64 = None;
    def base16(self, ciphertext):
        try:
            ciphertext = ciphertext.replace("=","") + "==="
            self.b16 = base64.b16decode(ciphertext).decode('ascii').upper()
        except (binascii.Error, UnicodeDecodeError) as e:
            pass
        return self.b16

    def base32(self, ciphertext):
        try:
            ciphertext = ciphertext.replace("=","") + "==="
            self.b32 = base64.b32decode(ciphertext).decode('ascii').upper()
        except (binascii.Error, UnicodeDecodeError) as e:
            pass
        return self.b32

    def base64(self, ciphertext):
        try:
            ciphertext = ciphertext.replace("=","") + "==="
            self.b64 = base64.b64decode(ciphertext).decode('ascii').upper()
        except (binascii.Error, UnicodeDecodeError) as e:
            pass
        return self.b64
