class InputOutString:
    def __init__(self):
        self.str = ""

    def getString(self):
        self.str = input("Please input a str:")

    def printString(self):
        print("str = %s" %self.str)