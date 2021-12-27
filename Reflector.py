class Rotor(object):

    def __init__(self, setting, startingPos):
        self.charList = ['d', 'g', 'u', 'a', 's', 'm', 'z', 'e', 'r', 'b', 'c', 'i', 'h', 'v', 'y', 'p', 'k', 'x', 'q', 'n', 't', 'f', 'w', 'l', 'o', 'j']


    def getEncriptChar(self, myChar):
        return self.charList[ord(myChar) - 97]