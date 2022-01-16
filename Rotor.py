class Rotor(object):

    def __init__(self, setting, startingPos):
        if(setting == 1):
            self.charList = ['e', 'k', 'm', 'f', 'l', 'g', 'd', 'q', 'v', 'z', 'n', 't', 'o', 'w', 'y', 'h', 'x', 'u', 's', 'p', 'a', 'i', 'b', 'r', 'c', 'j']

        elif(setting == 2):
            self.charList = ['a', 'j', 'd', 'k', 's', 'i', 'r', 'u', 'x', 'b', 'l', 'h', 'w', 't', 'm', 'c', 'q', 'g', 'z', 'n', 'p', 'y', 'f', 'v', 'o', 'e']

        elif(setting == 3):
            self.charList = ['b', 'd', 'f', 'h', 'j', 'l', 'c', 'p', 'r', 't', 'x', 'v', 'z', 'n', 'y', 'e', 'i', 'w', 'g', 'a', 'k', 'm', 'u', 's', 'q', 'o']
            
        else:
            self.charList = ['e', 'k', 'm', 'f', 'l', 'g', 'd', 'q', 'v', 'z', 'n', 't', 'o', 'w', 'y', 'h', 'x', 'u', 's', 'p', 'a', 'i', 'b', 'r', 'c', 'j']

        self.position = startingPos
        for x in range(1, startingPos):
            self.rotate()

    def rotate(self):
        tmp = self.charList[25]
        for x in range(25, 0, -1):
            self.charList[x] = self.charList[x - 1]
        self.charList[0] = tmp
        if(self.position == 26):
            self.position = 1
        else:
            self.position = self.position + 1

    def getEncriptChar(self, myChar):
        return self.charList[ord(myChar) - 97]

    def getReverseChar(self, myChar):
        i = 0
        while self.charList[i] != myChar:
            i = i + 1
        return (chr(i + 97))

    def getPos(self):
        return self.position

