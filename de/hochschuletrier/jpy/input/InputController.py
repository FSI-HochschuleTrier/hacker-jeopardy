__author__ = 'miko'
import sys
from de.hochschuletrier.jpy.console.JPYLogger import JPYLogger


class InputController:
    blockBuzzer = False

    def __init__(self, root):
        self.root = root
        self.logger = JPYLogger(self)
        self.logger.log("Input controller initialisiert")

        mainWindow = root.mainWindow


    def startGame(self, event):
        self.root.gameStarted = True
        self.root.gameStateManager.changeState(1)

    def userName(self, trigger):
        if self.root.gameStateManager.activeState != 1:
            return
        self.root.gameStateManager.states[1].overlayManager.overlays[1].insert(
            self.root.candidateManager.candidates[trigger])
        self.root.gameStateManager.states[1].overlayManager.overlays[1].user = self.root.candidateManager.candidates[
            trigger]
        self.root.gameStateManager.states[1].overlayManager.showOverlay(1)

    # warum ist hier das argument event?
    # def pressedBuzzer(self, event, trigger):
    def pressedBuzzer(self, trigger):
        print 'blocked=', self.blockBuzzer
        if InputController.blockBuzzer:
            return
        if self.root.gameStateManager.activeState == 0:
            return
        if not self.root.gameStarted:
            # ENTER USERNAME SUBROUTINE
            InputController.blockBuzzer = True
            self.logger.log(str(trigger) + " enter Name")
            self.userName(trigger)
        if not self.root.gameStateManager.states[1].overlayManager.overlays[0].isVisible:
            return
        else:
            self.root.questionManager.candidate = self.root.candidateManager.candidates[trigger]
            # self.root.gameStateManager.states[1].overlayManager.showOverlay(2)
            self.root.gameStateManager.states[1].overlayManager.overlays[0].highlight(
                self.root.questionManager.candidate.color)
            self.logger.prompt("Candidate :: " + str(trigger) + " ::  pressed Buzzer")
            InputController.blockBuzzer = True
            self.root.audioManager.pause()

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
            self.root.gameStateManager.states[1].overlayManager.overlays[0].hide(self)
            self.root.gameStateManager.states[1].double.lower()
            self.root.questionManager.toggledouble = False
            self.root.audioManager.stop()
            return
        if self.root.questionManager.toggledouble:
            self.root.questionManager.candidate.subPoints(2 * self.root.questionManager.worth)
        else:
            self.root.questionManager.candidate.subPoints(self.root.questionManager.worth)
        self.root.questionManager.candidate = None
        self.root.gameStateManager.states[1].overlayManager.overlays[0].normalize()
        # self.root.gameStateManager.states[1].overlayManager.overlays[0].hide(self)
        InputController.blockBuzzer = False
        self.root.audioManager.resumeBackgroundSong()

    def addPoints(self, event):
        if self.root.gameStateManager.activeState != 1:
            return
        if not self.root.gameStateManager.states[1].overlayManager.overlays[0].isVisible:
            return
        if self.root.questionManager.candidate is None:
            return
        if self.root.questionManager.toggledouble:
            self.root.questionManager.candidate.addPoints(2 * self.root.questionManager.worth)
        else:
            self.root.questionManager.candidate.addPoints(self.root.questionManager.worth)
        self.root.questionManager.toggledouble = False
        self.root.questionManager.candidate = None
        self.root.gameStateManager.states[1].overlayManager.overlays[0].hide(self)
        self.root.gameStateManager.states[1].double.lower()
        InputController.blockBuzzer = False
        self.root.audioManager.stop()