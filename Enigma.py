import Machine
from tkinter import *
from pathlib import Path

myMachine = Machine.Machine()
#myMachine.insertPlug('a','z')
#myMachine.insertPlug('e','f')
#myMachine.insertPlug('l','b')
#setting1 = input("please input your setting for rotor 1 ")
#setting2 = input("please input your setting for rotor 1 ")
#setting3 = input("please input your setting for rotor 1 ")
#myMachine.setRotorSetting(int(setting1), int(setting2), int(setting3))
#myChar = input("input your message that you would like to encript ")
#myChar = myMachine.encriptMessage(myChar)
#print(myChar)
#myChar = input("input your message that you would like to encript ")
#myChar = myMachine.encriptMessage(myChar)
#print(myChar)

root = Tk()
root.title("Enigma")
textForEncription = Entry(root, width = 40)
textForEncription.grid(row = 2, column = 0)
setting1 = Entry(root, width = 10)
setting1.grid(row = 1, column = 1)
setting2 = Entry(root, width = 10)
setting2.grid(row = 1, column = 2)
setting3 = Entry(root, width = 10)
setting3.grid(row = 1, column = 3)
order1 = Entry(root, width = 10)
order1.grid(row = 0, column = 1)
order2 = Entry(root, width = 10)
order2.grid(row = 0, column = 2)
order3 = Entry(root, width = 10)
order3.grid(row = 0, column = 3)
inputLabel = Label(root, width = 30)
inputLabel.grid(row = 3, column = 0)

def encriptButton():
    myMessage = myMachine.encriptMessage(textForEncription.get())
    inputLabel.config(text = myMessage)

def changeSettings():
    myMachine.setRotorSetting(int(setting1.get()), int(setting2.get()), int(setting3.get()))

def changeOrder():
    myMachine.setOrder(int(order1.get()), int(order2.get()), int(order3.get()))

encrButton = Button(root, text = "Encript Message", command = encriptButton)
encrButton.grid(row = 4, column = 0)
settButton = Button(root, text = "Change Settings", command = changeSettings)
settButton.grid(row = 1, column = 0)
orderButton = Button(root, text = "Change Order", command = changeOrder)
orderButton.grid(row = 0, column = 0)

root.mainloop()
