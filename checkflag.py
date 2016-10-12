import sys
class checkFlag():
    def __init__(self):
        ask_format = input("What is the format of your flags? ").upper()
        accepted = "ABCDEFGHIJKLMNOPQRSTVWXYZ"
        flag_format = ""
        for i in ask_format:
            if i in accepted:
                flag_format += i
        flag_format += "{"
        print(flag_format)

    def check(string):
        if(string.contains(self.flag_format)):
            print("Flag: " + string)
            sys.exit(0)
