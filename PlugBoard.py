class PlugBoard(object):
    
    def __init__(self):
        self.charList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.maxPlugs = 10
        self.plugs = 0
    
    def insertPlug(self, char1, char2):
        if self.plugs < self.maxPlugs and char1 != char2:
            self.charList[ord(char1) - 97] = char2
            self.charList[ord(char2) - 97] = char1
            self.plugs = self.plugs + 1

    def removePlug(self, myChar):
        if myChar != self.charList[ord(myChar) - 97]:
            tmp = self.charList[ord(myChar) - 97]
            self.charList[ord(myChar) - 97] = self.charList[ord(tmp) - 97]
            self.charList[ord(tmp) - 97] = tmp
            self.plugs = self.plugs - 1

    def checkForPlug(self, myChar):
        if myChar != self.charList[ord(myChar) - 97]:
            return True
        return False

    def getEncriptChar(self, myChar):
        return self.charList[ord(myChar) - 97]

    def getList(self):
        return self.charList

    def getNumPlugs(self):
        return self.plugs