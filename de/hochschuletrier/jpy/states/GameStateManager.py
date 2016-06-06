__author__ = 'miko'
from de.hochschuletrier.jpy.states.StartGameState import StartGameState
from de.hochschuletrier.jpy.states.PlayGameState import PlayGameState


class GameStateManager:
	def __init__(self, root):
		self.activeState = 0
		self.root = root
		self.states = []

		self.generateStates()
		self.changeState(0)

	def generateStates(self):
		self.states.append(StartGameState(self.root, stateName="Startbildschirm", id=0))
		self.states.append(PlayGameState(self.root, stateName="Hauptspiel", id=1))

	def changeState(self, state):
		if state > len(self.states) - 1:
			return
		self.states[self.activeState].lower()
		self.states[state].lift(aboveThis=None)
		self.activeState = state
