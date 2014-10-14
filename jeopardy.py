__author__ = 'MikO'

from de.hochschuletrier.jpy.states.GameStateManager import GameStateManager
from de.hochschuletrier.jpy.candidates.CandidateManager import CandidateManager
from de.hochschuletrier.jpy.questions.QuestionManager import QuestionManager
from de.hochschuletrier.jpy.ui.MainWindow import MainWindow
from de.hochschuletrier.jpy.backup.BackupManager import BackupManager
from de.hochschuletrier.jpy.input.PseudoInputController import PseudoInputController


class Jeopardy:
    def __init__(self):
        """
        array = [
            [1, 1, 1],
            [2, 2, 2],
            [3, 3, 3],
        ]

        temp = 0

        print array
        for x in range(0, len(array)):
            for y in range(x+1, len(array)):
                temp = array[y][x]
                array[y][x] = array[x][y]
                array[x][y] = temp

        print array
        """
        self.gameStarted = False
        self.mainWindow = MainWindow(self)
        self.backupManager = BackupManager(self)
        self.questionManager = QuestionManager(self, "questions.json")
        self.candidateManager = CandidateManager(self)
        self.gameStateManager = GameStateManager(self)
        self.inputController = PseudoInputController(self)

        self.mainWindow.mainloop()

def main():
    main = Jeopardy()

if __name__ == '__main__':
    main()
