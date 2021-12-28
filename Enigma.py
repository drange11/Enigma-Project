import Rotor
import Reflector

myRotor1 = Rotor.Rotor(1, 3)
myRotor2 = Rotor.Rotor(2, 5)
myRotor3 = Rotor.Rotor(3, 10)
myReflector = Reflector.Reflector()
myChar = myRotor1.getEncriptChar('z')
myChar = myRotor2.getEncriptChar(myChar)
myChar = myRotor3.getEncriptChar(myChar)
myChar = myReflector.getEncriptChar(myChar)
myChar = myRotor3.getReverseChar(myChar)
myChar = myRotor2.getReverseChar(myChar)
myChar = myRotor1.getReverseChar(myChar)
print(myChar)