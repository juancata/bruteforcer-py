from NLChar import NLChar

class NLString:

    def setString(string=['']):
        self.string = string

    def getString():
        return self.string

    def __init__(self):
        self.string = [NLChar(self, 0)]

    def value(self):
        aux = []
        for elem in self.string:
            aux.append(elem.value())
        return ''.join(aux)

    def next(self):
        self.string[0].next()
        return self.value()

    def increaseCharAt(self, index):
        if(index == len(self.string)):
            self.string.append(NLChar(self, len(self.string)))
        else:
            self.string[index].next()
