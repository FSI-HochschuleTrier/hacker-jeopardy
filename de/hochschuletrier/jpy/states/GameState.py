__author__ = 'miko'
from Tkinter import Frame


class GameState(Frame):
	def __init__(self, *args, **kwargs):
		self.stateName = kwargs["stateName"]
		self.root = args[0]
		self.id = kwargs["id"]
		Frame.__init__(self, self.root.mainWindow)
		self.config(
			background="gold"
		)
		self.place(relwidth=1, relheight=1)
