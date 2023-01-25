__author__ = 'miko'
from de.hochschuletrier.jpy.states.GameState import GameState
from de.hochschuletrier.jpy.Constants import Constants
from tkinter import Label, PhotoImage
import os.path
from PIL import Image


class StartGameState(GameState):
	def __init__(self, *args, **kwargs):
		GameState.__init__(self, *args, **kwargs)
		if not os.path.exists("resources/opener_temp.png"):
			image = Image.open("resources/opener.png")
			image = image.resize((Constants.SCREENW, Constants.SCREENH), Image.ANTIALIAS)
			image.save("resources/opener_temp.png", "png")
			print("generated")
		image2 = PhotoImage(file="resources/opener_temp.png")
		opener = Label(self)
		self.config(background="gold")
		opener.config(
			image=image2,
			background="#0000ff"
		)
		opener.image = image2
		opener.place(x=0, y=0, relwidth=1.0, relheight=1.0)
