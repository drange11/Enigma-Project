class Reflector(object):

    def __init__(self):
        self.charList = ['w', 'n', 't', 'e', 'd', 'm', 'z', 'q', 'r', 'p', 'x', 's', 'f', 'b', 'v', 'j', 'h', 'i', 'l', 'c', 'y', 'o', 'a', 'k', 'u', 'g']


    def getEncriptChar(self, myChar):
        return self.charList[ord(myChar) - 97]