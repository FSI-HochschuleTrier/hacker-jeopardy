__author__ = 'miko'
import sys
from de.hochschuletrier.jpy.console.JPYLogger import JPYLogger


class InputController:
	blockBuzzer = False
	introPlaying = False

	def __init__(self, root):
		self.root = root
		self.logger = JPYLogger(self)
		self.logger.log("Input controller initialisiert")

		mainWindow = root.mainWindow

	def startGame(self, event):
		if InputController.introPlaying:
			self.root.audioManager.stop("resources/intro.ogg")
			InputController.introPlaying = False
		self.root.gameStarted = True
		self.root.gameStateManager.changeState(1)

	def intro(self, event):
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
			self.root.audioManager.playFile('resources/buzzer.ogg')
		if not self.root.gameStateManager.states[1].overlayManager.overlays[0].isVisible:
			return
		else:
			self.root.questionManager.candidate = self.root.candidateManager.candidates[trigger]
			# self.root.gameStateManager.states[1].overlayManager.showOverlay(2)
			self.root.gameStateManager.states[1].overlayManager.overlays[0].highlight(
				self.root.questionManager.candidate.color)
			self.logger.prompt("Candidate :: " + str(trigger) + " ::  pressed Buzzer")
			InputController.blockBuzzer = True
			self.root.audioManager.pause(self.root.audioManager.backgroundsong)
			self.root.audioManager.playFile('resources/buzzer.ogg')

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
			self.root.audioManager.stop(self.root.audioManager.backgroundsong)
			return
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
		self.root.questionManager.candidate.addPoints(self.root.questionManager.worth)
		self.root.questionManager.candidate = None
		self.root.gameStateManager.states[1].overlayManager.overlays[0].hide(self)
		InputController.blockBuzzer = False
		self.root.audioManager.stop(self.root.audioManager.backgroundsong)
