class Morse:
    def morse(self, ciphertext):
        keepGing = True
        for i in range(len(ciphertext)):
            if(ciphertext[i] is "-" or ciphertext[i] is "." or ciphertext[i] is " "):
                keepGoing = True
            else:
                keepGoing = False
        if(keepGoing):
            CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
                    'D': '-..',    'E': '.',      'F': '..-.',
                    'G': '--.',    'H': '....',   'I': '..',
                    'J': '.---',   'K': '-.-',    'L': '.-..',
                    'M': '--',     'N': '-.',     'O': '---',
                    'P': '.--.',   'Q': '--.-',   'R': '.-.',
                    'S': '...',    'T': '-',      'U': '..-',
                    'V': '...-',   'W': '.--',    'X': '-..-',
                    'Y': '-.--',   'Z': '--..',

                    '0': '-----',  '1': '.----',  '2': '..---',
                    '3': '...--',  '4': '....-',  '5': '.....',
                    '6': '-....',  '7': '--...',  '8': '---..',
                    '9': '----.'
                    }
            CODE_REVERSED = {value:key for key,value in CODE.items()}
            thing = ''.join(CODE_REVERSED.get(i) for i in ciphertext.split())
            return thing
