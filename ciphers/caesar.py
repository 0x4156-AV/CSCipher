class Caesar:
    outcomes = []
    def caesar(self, message):
        message = message.upper()
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for key in range(len(LETTERS)):
            translated = ''
            for symbol in message:
                if symbol in LETTERS:
                    num = LETTERS.find(symbol)
                    num = num - key
                    if num < 0:
                        num = num + len(LETTERS)
                    translated = translated + LETTERS[num]
                else:
                    translated = translated + symbol
            self.outcomes.append(translated)

    def get_results(self):
        return self.outcomes
