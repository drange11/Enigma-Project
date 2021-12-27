class Rotor(object):

    def __init__(self, setting, startingPos):
        if(setting == 1):
            self.charList = ['d', 'g', 'u', 'a', 's', 'm', 'z', 'e', 'r', 'b', 'c', 'i', 'h', 'v', 'y', 'p', 'k', 'x', 'q', 'n', 't', 'f', 'w', 'l', 'o', 'j']

        elif(setting == 2):
            self.charList = ['u', 'r', 'h', 'm', 'v', 'n', 'g', 'f', 'y', 'x', 't', 'w', 'a', 'p', 'c', 'e', 'i', 'l', 's', 'o', 'g', 'd', 'k', 'z', 'j', 'b']

        elif(setting == 3):
            self.charList = ['t', 'j', 'l', 'v', 'y', 'h', 'w', 'i', 'g', 'd', 'f', 'u', 'c', 'a', 'x', 'z', 'n', 'g', 'b', 'r', 'm', 's', 'p', 'o', 'k', 'e']

        self.startingPos = startingPos
        self.currPos = startingPos

    def rotate(self):
        tmp = self.charList[25]
        for x in range(25, 0, -1):
            self.charList[x] = self.charList[x - 1]
        self.charList[0] = tmp

    def getEncriptChar(self, myChar):
        return self.charList[ord(myChar) - 97]


myRotor = Rotor(1, 0)
print(myRotor.getEncriptChar('a'))
myRotor.rotate()
print(myRotor.getEncriptChar('b'))