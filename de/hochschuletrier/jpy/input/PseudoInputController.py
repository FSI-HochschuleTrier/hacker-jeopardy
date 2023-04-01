__author__ = 'miko'
import sys
import signal
from de.hochschuletrier.jpy.console.JPYLogger import JPYLogger
from de.hochschuletrier.jpy.input.InputController import InputController


class PseudoInputController(InputController):
	def __init__(self, root):
		super().__init__(root)
		self.root = root
		self.logger = JPYLogger(self)
		self.logger.log("PseudoInputController initialisiert")
		self.blockBuzzer = False
		mainWindow = root.mainWindow
		#mainWindow.bind("<Escape>", self.endProgram)
		mainWindow.bind("<Control-c>", self.endProgram)
		mainWindow.bind("<KP_0>", lambda event: self.test(event, 0))
		mainWindow.bind("<KP_1>", lambda event: self.test(event, 1))
		mainWindow.bind("<KP_2>", lambda event: self.test(event, 2))
		mainWindow.bind("<KP_Add>", self.addPoints)
		mainWindow.bind("<KP_Subtract>", self.subPoints)
		mainWindow.bind("<KP_5>", self.intro)
		# mainWindow.bind("p", self.userName)
		mainWindow.bind("9", self.startGame)
		mainWindow.bind("1", lambda event: self.pressedBuzzer(0))
		mainWindow.bind("2", lambda event: self.pressedBuzzer(1))
		mainWindow.bind("3", lambda event: self.pressedBuzzer(2))
		mainWindow.bind("<Left>", self.root.gameStateManager.states[1].overlayManager.overlays[2].prevCandidate)
		mainWindow.bind("<Right>", self.root.gameStateManager.states[1].overlayManager.overlays[2].nextCandidate)

		signal.signal(signal.SIGINT, lambda x, y: mainWindow.quit())
