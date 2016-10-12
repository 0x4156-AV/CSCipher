class checkFlag(object):
    def __init__(slef):
        ask_format = input("What is the format of your flags? ").upper()
        accepted = "ABCDEFGHIJKLMNOPQRSTVWXYZ"
        flag_format = ""
        for i in ask_format:
            if i in accepted:
                flag_format += i
