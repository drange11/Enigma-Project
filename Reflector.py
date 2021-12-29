class Reflector(object):

    def __init__(self):
        self.charList = ['y', 'r', 'u', 'h', 'q', 's', 'l', 'd', 'p', 'x', 'n', 'g', 'o', 'k', 'm', 'i', 'e', 'b', 'f', 'z', 'c', 'w', 'v', 'j', 'a', 't']


    def getEncriptChar(self, myChar):
        return self.charList[ord(myChar) - 97]