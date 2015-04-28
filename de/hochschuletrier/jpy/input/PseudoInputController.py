__author__ = 'miko'
import sys
from de.hochschuletrier.jpy.console.JPYLogger import JPYLogger
from de.hochschuletrier.jpy.input.InputController import InputController


class PseudoInputController(InputController):
    def __init__(self,root):
        self.logger = JPYLogger(self)
        self.logger.log("PseudoInputController initialisiert")
        self.blockBuzzer = False
        mainWindow = root.mainWindow
        mainWindow.bind("<Escape>", self.endProgram)
        mainWindow.bind("<KP_0>", lambda event: self.test(event, 0))
        mainWindow.bind("<KP_1>", lambda event: self.test(event, 1))
        mainWindow.bind("<KP_2>", lambda event: self.test(event, 2))
        mainWindow.bind("<KP_Add>", self.addPoints)
        mainWindow.bind("<KP_Subtract>", self.subPoints)
        #mainWindow.bind("p", self.userName)
        mainWindow.bind("9", self.startGame)
        mainWindow.bind("1", lambda event: self.pressedBuzzer(event, 0))
        mainWindow.bind("2", lambda event: self.pressedBuzzer(event, 1))
        mainWindow.bind("3", lambda event: self.pressedBuzzer(event, 2))