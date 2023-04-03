#!/usr/bin/env python

__author__ = 'MikO'

import sys
from de.hochschuletrier.jpy.states.GameStateManager import GameStateManager
from de.hochschuletrier.jpy.candidates.CandidateManager import CandidateManager
from de.hochschuletrier.jpy.questions.QuestionManager import QuestionManager
from de.hochschuletrier.jpy.ui.MainWindow import MainWindow
from de.hochschuletrier.jpy.backup.BackupManager import BackupManager
from de.hochschuletrier.jpy.input.PseudoInputController import PseudoInputController
from de.hochschuletrier.jpy.input.BuzzerInputController import BuzzerInputController
from de.hochschuletrier.jpy.audio.AudioManager import AudioManager


class Jeopardy:
	def __init__(self, questiondir, numPlayers, debug = ""):
		if (debug == "debug"):
			self.debug = True
		else:
			self.debug = False
		self.gameStarted = False
		self.mainWindow = MainWindow(self)
		self.backupManager = BackupManager(self)
		# self.questionManager = QuestionManager(self, "questions.json")
		self.questionManager = QuestionManager(self, questiondir)
		self.candidateManager = CandidateManager(self, numPlayers)
		self.gameStateManager = GameStateManager(self)
		self.inputController = PseudoInputController(self)
		self.buzzerInputController = BuzzerInputController(self)
		self.audioManager = AudioManager(self)

		self.mainWindow.mainloop()

def main(argc, argv):
	players = 4
	debug   = ""
	if argc > 2:
		players = int(argv[2])
		if argc > 3:
			debug = argv[3]
	main = Jeopardy(argv[1], players, debug)


if __name__ == '__main__':
	main(len(sys.argv), sys.argv)
