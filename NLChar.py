class NLChar:

    def setChar(self, char=""):
        self.char = char

    def getChar(self):
        return self.char

    def __init__(self, string, string_index, start_index = 33, last_index = 126):
        self.start_index = start_index
        self.last_index = last_index
        self.string = string
        self.string_index = string_index
        self.char = chr(self.start_index)

    def value(self):
        return self.char

    def next(self):
        if (((ord(self.char)) % self.last_index) is 0):
            self.char = chr(self.start_index)
            self.string.increaseCharAt(self.string_index + 1)
        else:
            self.char = chr(ord(self.char)+1)
        return self.char
