__author__ = 'MikO'

from de.hochschuletrier.jpy.states.GameStateManager import GameStateManager
from de.hochschuletrier.jpy.candidates.CandidateManager import CandidateManager
from de.hochschuletrier.jpy.questions.QuestionManager import QuestionManager
from de.hochschuletrier.jpy.ui.MainWindow import MainWindow
from de.hochschuletrier.jpy.backup.BackupManager import BackupManager
from de.hochschuletrier.jpy.input.PseudoInputController import PseudoInputController
from de.hochschuletrier.jpy.audio.AudioManager import AudioManager


class Jeopardy:
    def __init__(self):
        self.gameStarted = False
        self.mainWindow = MainWindow(self)
        self.backupManager = BackupManager(self)
        # self.questionManager = QuestionManager(self, "questions.json")
        self.questionManager = QuestionManager(self, "test.json")
        self.candidateManager = CandidateManager(self)
        self.gameStateManager = GameStateManager(self)
        self.inputController = PseudoInputController(self)
        self.audioManager = AudioManager(self)

        self.mainWindow.mainloop()


def main():
    main = Jeopardy()


if __name__ == '__main__':
    main()
