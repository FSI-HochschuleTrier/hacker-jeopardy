from Tkinter import *
from de.hochschuletrier.jpy.Constants import Constants, Fonts
from math import *


class JPYUserLabel(Frame):
	def __init__(self, *args, **kwargs):
		Frame.__init__(self, *args)
		self.label = ""
		self.nLabel = ""
		self.user = kwargs["user"]
		self.nameFont = Fonts.USER_LABEL_NAME
		self.pointsFont = Fonts.MONEY_MEDIUM
		self.bgcolor = kwargs["back"]
		self.width = len(self.master.root.candidateManager.candidates)
		if self.width > 3:
			self.width = 6
		self.config(
			width=Constants.SCREENW / self.width + 1,
			height=Constants.SCREENH / 7,
			background="black",
			pady=5,
			padx=5,
			cursor="man"
		)
		self.pack_propagate(0)
		self.pointsLabel()
		self.nameLabel()

	def nameLabel(self):
		self.nLabel = Label(self)
		self.nLabel.config(
			textvariable=self.user.name,
			background=self.bgcolor,
			foreground="white",
			bd=0,
			relief="solid",
			font=self.nameFont,
			wraplength=Constants.SCREENW / self.width
		)
		self.nLabel.pack(fill=BOTH, expand=1)

	def pointsLabel(self):
		self.label = Label(self)
		# self.label.bind("<Button-1>", self.edit.show(self.user))
		self.label.config(
			textvariable=self.user.points,
			background=self.bgcolor,
			foreground="white",
			bd=0,
			relief="solid",
			font=self.pointsFont,
			wraplength=Constants.SCREENW / self.width
		)
		self.label.pack(fill=BOTH, expand=1)
