__author__ = 'miko'
import sys
from de.hochschuletrier.jpy.console.JPYLogger import JPYLogger


class PseudoInputController:
    def __init__(self, root):
        self.root = root
        self.logger = JPYLogger(self)
        self.logger.log("Input controller initialisiert")
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

    def startGame(self, event):
        self.root.gameStarted = True
        self.root.gameStateManager.changeState(1)

    def userName(self, trigger):
        if self.root.gameStateManager.activeState != 1:
            return
        self.root.gameStateManager.states[1].overlayManager.overlays[1].insert(self.root.candidateManager.candidates[trigger])
        self.root.gameStateManager.states[1].overlayManager.overlays[1].user = self.root.candidateManager.candidates[trigger]
        self.root.gameStateManager.states[1].overlayManager.showOverlay(1)

    def pressedBuzzer(self, event, trigger):
        if self.blockBuzzer:
            return
        if self.root.gameStateManager.activeState == 0:
            return
        if not self.root.gameStarted:
            # ENTER USERNAME SUBROUTINE
            self.blockBuzzer = True
            self.logger.log(str(trigger) + " enter Name")
            self.userName(trigger)
        if not self.root.gameStateManager.states[1].overlayManager.overlays[0].isVisible:
            return
        else:
            self.root.questionManager.candidate = self.root.candidateManager.candidates[trigger]
            self.logger.prompt("Candidate :: " + str(trigger) + " ::  pressed Buzzer")
            self.blockBuzzer = True

    def endProgram(self, event):
        if self.root.gameStateManager.activeState == 0:
            return
        sys.exit()

    def test(self, event, trigger):
        self.root.gameStateManager.changeState(trigger)

    def subPoints(self, event):
        if self.root.gameStateManager.activeState != 1:
            return
        if not self.root.gameStateManager.states[1].overlayManager.overlays[0].isVisible:
            return
        if self.root.questionManager.candidate is None:
            return
        self.root.questionManager.candidate.subPoints(self.root.questionManager.worth)
        self.root.gameStateManager.states[1].overlayManager.overlays[0].hide(self)
        self.blockBuzzer = False

    def addPoints(self, event):
        if self.root.gameStateManager.activeState != 1:
            return
        if not self.root.gameStateManager.states[1].overlayManager.overlays[0].isVisible:
            return
        if self.root.questionManager.candidate is None:
            return
        self.root.questionManager.candidate.addPoints(self.root.questionManager.worth)
        self.root.gameStateManager.states[1].overlayManager.overlays[0].hide(self)
        self.blockBuzzer = False