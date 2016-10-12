import sys
class checkFlag():
    flag_format="";
    def __init__(self):
        ask_format = input("What is the format of your flags? ").upper()
        accepted = "ABCDEFGHIJKLMNOPQRSTVWXYZ"
        for i in ask_format:
            if i in accepted:
                self.flag_format += i

    def check(self,string):
        if(string) == None:
            pass
        elif(self.flag_format in string):
            print("Flag: " + string)
            sys.exit(0)

    def check_array(self,array):
        for i in range(len(array)):
            if(self.flag_format in array[i]):
                print("Flag: " + array[i])
                sys.exit(0)
