class Baconain:
    def baconain(self, ciphertext):
        keepGing = True
        for i in range(len(ciphertext)):
            if(ciphertext[i] is "A" or ciphertext[i] is "B"):
                keepGoing = True
            elif(ciphertext[i] is "I" or ciphertext[i] is "J"):
                keepGoing = True
            elif(ciphertext[i] is "U" or ciphertext[i] is "V"):
                keepGoing = True
            else:
                keepGoing = False
        if(keepGoing):
            if(ciphertext[5] != " "):
                ciphertext = " ".join(ciphertext[i:i+5] for i in range(0, len(ciphertext), 5))
            print(ciphertext)
            CODE = {'A': 'AAAAA',     'B': 'AAAAB',      'C': 'AAABA',
                    'D': 'AAABB',     'E': 'AABAA',      'F': 'AABAB',
                    'G': 'AABBA',     'H': 'AABBB',      'I': 'ABAAA',
                    'J': 'ABAAA',     'K': 'ABAAB',      'L': 'ABABA',
                    'M': 'ABABB',     'N': 'ABBAA',      'O': 'ABBAB',
                    'P': 'ABBBA',     'Q': 'ABBBB',      'R': 'BAAAA',
                    'S': 'BAAAB',     'T': 'BAABA',      'U': 'BAABB',
                    'V': 'BAABB',     'W': 'BABAA',      'X': 'BABAB',
                    'Y': 'BABBA',     'Z': 'BABBB'
                    }
            CODE_REVERSED = {value:key for key,value in CODE.items()}
            print(CODE_REVERSED)
            thing = ''.join(CODE_REVERSED.get(i) for i in ciphertext.split())
            return thing
