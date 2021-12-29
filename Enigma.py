import TopGroup

myTopGroup = TopGroup.TopGroup()
setting1 = input("please input your setting for rotor 1 ")
setting2 = input("please input your setting for rotor 1 ")
setting3 = input("please input your setting for rotor 1 ")
myTopGroup.setRotorSetting(int(setting1), int(setting2), int(setting3))
myChar = input("input your message that you would like to encript ")
myChar = myTopGroup.encriptMessage(myChar)
print(myChar)
myChar = input("input your message that you would like to encript ")
myChar = myTopGroup.encriptMessage(myChar)
print(myChar)
