__author__ = 'miko'
from Tkinter import *
from de.hochschuletrier.jpy.states.GameStateManager import GameStateManager
from de.hochschuletrier.jpy.candidates.CandidateManager import CandidateManager
from de.hochschuletrier.jpy.questions.QuestionManager import QuestionManager
from de.hochschuletrier.jpy.ui.MainWindow import MainWindow
from de.hochschuletrier.jpy.input.PseudoInputController import PseudoInputController
from de.hochschuletrier.jpy.console.JPYLogger import JPYLogger


SCREENW = 0
SCREENH = 0

class Jeopardy:
    def __init__(self):
        self.gameStarted = False
        self.mainWindow = MainWindow(self)
        self.questionManager = QuestionManager("questions.json")
        self.candidateManager = CandidateManager(self)
        self.gameStateManager = GameStateManager(self)
        self.inputController = PseudoInputController(self)
        logger = JPYLogger(self)
        logger.log("Dies ist ein Test")

        #self.mainWindow.bind("<KP_9>", self.gameStateManager.states[1].overlayManager.overlays[0].hide)
        #self.mainWindow.after(1000, self.test)
        self.mainWindow.mainloop()

    def test(self):
        print "test"
        self.mainWindow.after(1000, self.test)

def main():
    main = Jeopardy()

if __name__ == '__main__':
    main()
