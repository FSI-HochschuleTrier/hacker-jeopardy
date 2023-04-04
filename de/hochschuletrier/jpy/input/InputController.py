__author__ = 'miko'
import sys
from tkinter import Tk
from de.hochschuletrier.jpy.console.JPYLogger import JPYLogger
from de.hochschuletrier.jpy.input.Buzzer import ResetBuzzerLEDs


class InputController:
	blockBuzzer = False
	introPlaying = False

	def __init__(self, root):
		self.root = root
		self.logger = JPYLogger(self)
		self.logger.log("Input controller initialisiert")
		self.gpio = None

		if not (root.debug):
			import RPi.GPIO as GPIO
			self.gpio = GPIO

		mainWindow = root.mainWindow

	def startGame(self, event = None):
		if InputController.introPlaying:
			self.root.audioManager.stop(None)
			InputController.introPlaying = False
		self.root.gameStarted = True
		self.root.gameStateManager.changeState(1)

	def intro(self, event = None):
		if self.root.gameStateManager.activeState != 0:
			return
		# VIDEO IS WORKING!
		#self.root.audioManager.playFile("resources/tt.mp4")
		if InputController.introPlaying:
			self.root.audioManager.stop("resources/intro.ogg")
			InputController.introPlaying = False
		else:
			self.root.audioManager.playFile("resources/intro.ogg")
			InputController.introPlaying = True

	def userName(self, trigger):
		if self.root.gameStateManager.activeState != 1:
			return
		self.root.gameStateManager.states[1].overlayManager.overlays[1].insert(
			self.root.candidateManager.candidates[trigger])
		self.root.gameStateManager.states[1].overlayManager.overlays[1].user = self.root.candidateManager.candidates[
			trigger]
		self.root.gameStateManager.states[1].overlayManager.showOverlay(1)

	def releaseBuzzer(self):
		InputController.blockBuzzer = False

		if not self.root.debug and self.gpio != None:
			ResetBuzzerLEDs(self.gpio)

	# warum ist hier das argument event?
	# def pressedBuzzer(self, event, trigger):
	def pressedBuzzer(self, trigger):
		#print('blocked=', InputController.blockBuzzer)
		if InputController.blockBuzzer:
			return False
		if self.root.gameStateManager.activeState == 0:
			return False
		if not self.root.gameStarted:
			# ENTER USERNAME SUBROUTINE
			InputController.blockBuzzer = True
			self.logger.log(str(trigger) + " enter Name")
			self.userName(trigger)
			#self.root.audioManager.playFile('resources/buzzer.ogg')
			self.root.audioManager.playBuzzer()
			return True
		if not self.root.gameStateManager.states[1].overlayManager.overlays[0].isVisible:
			return False
		else:
			InputController.blockBuzzer = True
			self.root.audioManager.stopQuestion()
			self.root.questionManager.candidate = self.root.candidateManager.candidates[trigger]
			# self.root.gameStateManager.states[1].overlayManager.showOverlay(2)
			self.root.gameStateManager.states[1].overlayManager.overlays[0].highlight(
				self.root.questionManager.candidate.color)
			self.logger.prompt("Candidate :: " + str(trigger) + " ::  pressed Buzzer")
			#self.root.audioManager.pause(None)
			self.root.audioManager.pauseBackgroundSong()
			self.root.audioManager.playBuzzer()
		return True

	def endProgram(self, event, _ = None):
		if self.root.gameStateManager.activeState == 0:
			return
		sys.exit()

	def test(self, event, trigger):
		self.root.gameStateManager.changeState(trigger)

	def subPoints(self, event = None):
		#self.logger.prompt(str(self.root.gameStateManager.states[1].overlayManager.overlays[2].settedPoints))
		#self.logger.prompt(str(self.root.questionManager.candidate is None))

		if self.root.gameStateManager.activeState != 1:
			return
		if not self.root.gameStateManager.states[1].overlayManager.overlays[0].isVisible:
			return
		if self.root.questionManager.candidate is None:
			self.root.gameStateManager.states[1].overlayManager.overlays[0].stopAudio()
			self.root.gameStateManager.states[1].overlayManager.overlays[0].hide(self)
			self.root.gameStateManager.states[1].overlayManager.overlays[2].hide(self)
			if self.root.gameStateManager.states[1].overlayManager.overlays[0].audio == "":
				self.root.audioManager.stopBackgroundSong()
			return
		if self.root.gameStateManager.states[1].overlayManager.overlays[0].audio != "":
			self.root.gameStateManager.states[1].overlayManager.overlays[0].playAudio()
		if self.root.gameStateManager.states[1].overlayManager.overlays[2].settedPoints != 0:
			self.root.questionManager.candidate.subPoints(self.root.gameStateManager.states[1].overlayManager.overlays[2].settedPoints)
			self.root.gameStateManager.states[1].overlayManager.overlays[2].settedPoints = 0
		else:
			self.root.questionManager.candidate.subPoints(self.root.questionManager.worth)
		self.root.questionManager.candidate = None
		self.root.gameStateManager.states[1].overlayManager.overlays[0].normalize()
		# self.root.gameStateManager.states[1].overlayManager.overlays[0].hide(self)
		self.releaseBuzzer()
		if self.root.gameStateManager.states[1].overlayManager.overlays[0].audio == "":
			self.root.audioManager.playBackgroundSong()

	def addPoints(self, event = None):
		if self.root.gameStateManager.activeState != 1:
			return
		if not self.root.gameStateManager.states[1].overlayManager.overlays[0].isVisible:
			return
		if self.root.questionManager.candidate is None and self.root.gameStateManager.states[1].overlayManager.overlays[0].audio != "":
			self.root.gameStateManager.states[1].overlayManager.overlays[0].playAudio()
			return
		if self.root.questionManager.candidate is None:
			return
		self.root.gameStateManager.states[1].overlayManager.overlays[0].stopAudio()
		if self.root.gameStateManager.states[1].overlayManager.overlays[2].settedPoints != 0:
			self.root.questionManager.candidate.addPoints(self.root.gameStateManager.states[1].overlayManager.overlays[2].settedPoints)
			self.root.gameStateManager.states[1].overlayManager.overlays[2].settedPoints = 0
		else:
			self.root.questionManager.candidate.addPoints(self.root.questionManager.worth)
		self.root.questionManager.lastButton.highlight(self.root.questionManager.candidate.color)
		Tk.update(self.root.mainWindow)
		self.root.questionManager.candidate = None
		self.root.gameStateManager.states[1].overlayManager.overlays[0].hide(self)
		self.releaseBuzzer()
		self.root.audioManager.stopBackgroundSong()
