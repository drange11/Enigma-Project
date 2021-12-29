import Rotor
import Reflector

class TopGroup(object):

    def __init__(self):
        self.count1 = 0
        self.count2 = 0
        self.myRotor1 = Rotor.Rotor(1, 0)
        self.myRotor2 = Rotor.Rotor(2, 0)
        self.myRotor3 = Rotor.Rotor(3, 0)
        self.myReflector = Reflector.Reflector()

    def setRotorSetting(self, setting1, setting2, setting3):
        self.myRotor1 = Rotor.Rotor(1, setting1)
        self.myRotor2 = Rotor.Rotor(2, setting2)
        self.myRotor3 = Rotor.Rotor(3, setting3)

    def encriptChar(self, myChar):
        if myChar.isalpha() == False:
            return myChar
        if myChar.isupper():
            myChar = myChar.lower()
        myChar = self.myRotor1.getEncriptChar(myChar)
        myChar = self.myRotor2.getEncriptChar(myChar)
        myChar = self.myRotor3.getEncriptChar(myChar)
        myChar = self.myReflector.getEncriptChar(myChar)
        myChar = self.myRotor3.getReverseChar(myChar)
        myChar = self.myRotor2.getReverseChar(myChar)
        myChar = self.myRotor1.getReverseChar(myChar)
        self.doRotates()
        return myChar

    def doRotates(self):
        self.count1 = self.count1 + 1
        self.myRotor1.rotate()
        if self.count1 > 24:
            self.count2 = self.count2 + 1
            self.count1 = 0
            self.myRotor2.rotate()
            if self.count2 > 24:
                self.count2 = 0
                self.myRotor3.rotate()
    
    def encriptMessage(self, myMessage):
        tmpMessage = ''
        for x in range(0, len(myMessage)):
            tmpMessage = tmpMessage + self.encriptChar(myMessage[x])
        return tmpMessage

