import Machine
from tkinter import *

class machineGUIControl(object):
    def __init__(self):
        self.myMachine = Machine.Machine()
        self.root = Tk()
        self.root.title("Enigma")
        self.setupPlugControl()
        self.setupSettingControl()
        self.setupOrderControl()
        self.setupEncription()
        self.setupButtons()
        self.root.mainloop()

    def setupPlugControl(self):
        self.plug1 = Entry(self.root, width = 10)
        self.plug1.grid(row = 5, column = 2)
        self.plug2 = Entry(self.root, width = 10)
        self.plug2.grid(row = 5, column = 3)
        self.plugLabel = Label(self.root, width = 40, text = 'Plugs: ' + self.myMachine.getPlugBoard())
        self.plugLabel.grid(row = 5, column = 0)
        self.plugNumLabel = Label(self.root, width = 8, text = '0/10')
        self.plugNumLabel.grid(row = 6, column = 1)

    def setupSettingControl(self):
        self.setting1 = Entry(self.root, width = 10)
        self.setting1.grid(row = 1, column = 1)
        self.setting2 = Entry(self.root, width = 10)
        self.setting2.grid(row = 1, column = 2)
        self.setting3 = Entry(self.root, width = 10)
        self.setting3.grid(row = 1, column = 3)
        self.set1Label = Label(self.root, width = 4, text = self.myMachine.getSetting(1))
        self.set1Label.grid(row = 2, column = 1)
        self.set2Label = Label(self.root, width = 4, text = self.myMachine.getSetting(1))
        self.set2Label.grid(row = 2, column = 2)
        self.set3Label = Label(self.root, width = 4, text = self.myMachine.getSetting(1))
        self.set3Label.grid(row = 2, column = 3)


    def setupOrderControl(self):
        self.order1 = Entry(self.root, width = 10)
        self.order1.grid(row = 0, column = 1)
        self.order2 = Entry(self.root, width = 10)
        self.order2.grid(row = 0, column = 2)
        self.order3 = Entry(self.root, width = 10)
        self.order3.grid(row = 0, column = 3)

    def setupEncription(self):
        self.textForEncription = Entry(self.root, width = 40)
        self.textForEncription.grid(row = 3, column = 0)
        self.separationLabel = Label(self.root, width = 40, text = '---------------------------------------------')
        self.separationLabel.grid(row = 2, column = 0)
        self.inputLabel = Label(self.root, width = 30)
        self.inputLabel.grid(row = 4, column = 0)
        
    def encriptButton(self):
        myMessage = self.myMachine.encriptMessage(self.textForEncription.get())
        self.inputLabel.config(text = myMessage)
        self.set1Label.config(text = self.myMachine.getSetting(1))
        self.set2Label.config(text = self.myMachine.getSetting(2))
        self.set3Label.config(text = self.myMachine.getSetting(3))

    def changeSettings(self):
        self.myMachine.setRotorSetting(int(self.setting1.get()), int(self.setting2.get()), int(self.setting3.get()))
        self.set1Label.config(text = self.myMachine.getSetting(1))
        self.set2Label.config(text = self.myMachine.getSetting(2))
        self.set3Label.config(text = self.myMachine.getSetting(3))

    def changeOrder(self):
        self.myMachine.setOrder(int(self.order1.get()), int(self.order2.get()), int(self.order3.get()))

    def insertPlug(self):
        self.myMachine.insertPlug(self.plug1.get(), self.plug2.get())
        self.plugLabel.config(text = 'Plugs: ' + self.myMachine.getPlugBoard())
        self.plugNumLabel.config(text = str(self.myMachine.getNumPlugs()) + '/10')

    def setupButtons(self):
        self.encrButton = Button(self.root, text = "Encript Message", command = self.encriptButton)
        self.encrButton.grid(row = 6, column = 0)
        self.settButton = Button(self.root, text = "Change Settings", command = self.changeSettings)
        self.settButton.grid(row = 1, column = 0)
        self.orderButton = Button(self.root, text = "Change Order", command = self.changeOrder)
        self.orderButton.grid(row = 0, column = 0)
        self.plugButton = Button(self.root, text = "Add Plug", command = self.insertPlug, width = 8)
        self.plugButton.grid(row = 5, column = 1)


enigmaProgram = machineGUIControl()



