#!/usr/bin/env python

__author__ = 'MikO'

import sys
import pyglet
import platform
from threading import Thread
from de.hochschuletrier.jpy.states.GameStateManager import GameStateManager
from de.hochschuletrier.jpy.candidates.CandidateManager import CandidateManager
from de.hochschuletrier.jpy.questions.QuestionManager import QuestionManager
from de.hochschuletrier.jpy.ui.MainWindow import MainWindow
from de.hochschuletrier.jpy.backup.BackupManager import BackupManager
from de.hochschuletrier.jpy.input.PseudoInputController import PseudoInputController
from de.hochschuletrier.jpy.input.BuzzerInputController import BuzzerInputController
from de.hochschuletrier.jpy.audio.AudioManager import AudioManager


class Jeopardy:
	def __init__(self, questiondir, debug = ""):
		if (debug == "debug"):
			self.debug = True
		else:
			self.debug = False
		self.gameStarted = False
		self.mainWindow = MainWindow(self)
		self.backupManager = BackupManager(self)
		# self.questionManager = QuestionManager(self, "questions.json")
		self.questionManager = QuestionManager(self, questiondir)
		self.candidateManager = CandidateManager(self)
		self.gameStateManager = GameStateManager(self)
		self.inputController = PseudoInputController(self)
		self.buzzerInputController = BuzzerInputController(self)
		self.audioManager = AudioManager(self)

		# pumping `pyglet`'s mainloop
		if platform.system() != "Darwin":
			audioThread = Thread(target=pyglet.app.run)
			audioThread.start()


		self.mainWindow.mainloop()

def main(argv):
	if (len(argv) > 2):
		main = Jeopardy(argv[1], argv[2])
	else:
		main = Jeopardy(argv[1])


if __name__ == '__main__':
	main(sys.argv)
