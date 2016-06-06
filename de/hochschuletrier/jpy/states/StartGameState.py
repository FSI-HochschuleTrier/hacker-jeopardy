__author__ = 'miko'
from de.hochschuletrier.jpy.states.GameState import GameState
from Tkinter import Label, PhotoImage


class StartGameState(GameState):
	def __init__(self, *args, **kwargs):
		GameState.__init__(self, *args, **kwargs)
		image = PhotoImage(file="resources/opener.gif")
		opener = Label(self)
		self.config(background="gold")
		opener.config(
			image=image,
			background="blue"
		)
		opener.image = image
		opener.place(x=0, y=0, relwidth=1, relheight=1)
