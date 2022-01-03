import Rotor
import Reflector
import PlugBoard

class Machine(object):

    def __init__(self):
        self.count1 = 0
        self.count2 = 0
        self.myRotor1 = Rotor.Rotor(1, 0)
        self.myRotor2 = Rotor.Rotor(2, 0)
        self.myRotor3 = Rotor.Rotor(3, 0)
        self.myReflector = Reflector.Reflector()
        self.myPlug = PlugBoard.PlugBoard()
        self.setting1 = 0
        self.setting2 = 0
        self.setting3 = 0
        self.rotor1 = 1
        self.rotor2 = 2
        self.rotor3 = 3

    def setRotorSetting(self, setting1, setting2, setting3):
        self.myRotor1 = Rotor.Rotor(self.rotor1, setting1)
        self.myRotor2 = Rotor.Rotor(self.rotor2, setting2)
        self.myRotor3 = Rotor.Rotor(self.rotor3, setting3)
        self.count1 = setting1
        self.count2 = setting2
        self.setting1 = setting1
        self.setting2 = setting2
        self.setting3 = setting3

    def setOrder(self, rotorNum1, rotorNum2, rotorNum3):
        self.myRotor1 = Rotor.Rotor(rotorNum1, self.setting1)
        self.myRotor2 = Rotor.Rotor(rotorNum2, self.setting2)
        self.myRotor3 = Rotor.Rotor(rotorNum3, self.setting3)
        self.count1 = self.setting1
        self.count2 = self.setting2
        self.rotor1 = rotorNum1
        self.rotor2 = rotorNum2
        self.rotor3 = rotorNum3

    def encriptChar(self, myChar):
        if myChar.isalpha() == False:
            return myChar
        if myChar.isupper():
            myChar = myChar.lower()
        myChar = self.myPlug.getEncriptChar(myChar)
        myChar = self.myRotor1.getEncriptChar(myChar)
        myChar = self.myRotor2.getEncriptChar(myChar)
        myChar = self.myRotor3.getEncriptChar(myChar)
        myChar = self.myReflector.getEncriptChar(myChar)
        myChar = self.myRotor3.getReverseChar(myChar)
        myChar = self.myRotor2.getReverseChar(myChar)
        myChar = self.myRotor1.getReverseChar(myChar)
        myChar = self.myPlug.getEncriptChar(myChar)
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

    def insertPlug(self, char1, char2):
        self.myPlug.insertPlug(char1, char2)

    def removePlug(self, char1, char2):
        self.myPlug.removePlug(char1, char2)
