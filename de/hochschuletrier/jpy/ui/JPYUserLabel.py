from tkinter import Frame, Label, BOTH, X
from de.hochschuletrier.jpy.Constants import Constants, Fonts
from math import *


class JPYUserLabel(Frame):
	def __init__(self, parent, user, back, numPlayers):
		super().__init__(parent)
		self.label = ""
		self.nLabel = ""
		self.numPlayers = numPlayers
		self.user = user
		self.nameFont = Fonts.USER_LABEL_NAME
		self.pointsFont = Fonts.MONEY_MEDIUM
		self.bgcolor = back
		self.config(
			height=Constants.SCREENH / 7,
			background="black",
			pady=7,
			padx=5,
			cursor="man"
		)
		self.pointsLabel()
		self.nameLabel()

	def nameLabel(self):
		self.nLabel = Label(self)
		self.nLabel.config(
			textvariable=self.user.name,
			background=self.bgcolor,
			foreground="#222",
			bd=0,
			relief="solid",
			font=self.nameFont,
			wraplength=(Constants.SCREENW / self.numPlayers) / 2
		)
		self.nLabel.pack(fill=X, expand=False)

	def pointsLabel(self):
		self.label = Label(self)
		self.label.config(
			textvariable=self.user.points,
			background=self.bgcolor,
			foreground="#222",
			bd=0,
			relief="solid",
			font=self.pointsFont,
			wraplength=(Constants.SCREENW / self.numPlayers) / 2
		)
		self.label.pack(fill=BOTH, expand=True)
