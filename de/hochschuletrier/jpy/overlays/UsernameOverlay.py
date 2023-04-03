from de.hochschuletrier.jpy.input.InputController import InputController

__author__ = 'miko'
from de.hochschuletrier.jpy.Constants import Fonts
from de.hochschuletrier.jpy.overlays.Overlay import Overlay
from de.hochschuletrier.jpy.console.JPYLogger import JPYLogger
from tkinter import Label, Entry, Button, END


class UsernameOverlay(Overlay):
	def __init__(self, *args, **kwargs):
		Overlay.__init__(self, *args, **kwargs)
		self.label = None
		self.field = None
		self.button = None
		self.user = None
		self.spacer = None
		self.logger = JPYLogger(self)
		self.config(
			background="gold",
			cursor="arrow"
		)

		self.renderLabel()
		self.renderField()
		self.renderButton()

	def renderLabel(self):
		self.label = Label(self)
		self.label.config(
			text="CHANGE PLAYERNAME",
			font=Fonts.MONEY_BIG,
			background="gold"
		)
		self.label.pack()

	def renderField(self):
		self.field = Entry(self)
		self.field.config(
			relief="solid",
			bd=2,
			highlightcolor="black",
			font=Fonts.USER_LABEL_NAME_BIG
		)
		self.field.bind("<Return>", self.save)
		self.field.focus_set()
		self.field.pack()

	def renderButton(self):
		self.spacer = Label(self, text='\n', background="gold").pack()
		self.button = Button(self)
		self.button.config(
			text="OK",
			relief="solid",
			background="black",
			foreground="gold",
			font=Fonts.MONEY_MEDIUM,
			command=self.save
		)
		self.button.pack()

	def save(self, event=""):
		self.logger.prompt("User " + str(self.user.id) + " changed name from '" + self.user.name.get() + "' to '" + self.field.get() + "'")
		self.user.name.set(self.field.get())
		self.hide(self)
		self.root.root.inputController.releaseBuzzer()

	def insert(self, user):
		self.config(bg=user.color)
		self.label.config(bg=user.color)
		self.spacer.config(bg=user.color)
		self.button.config(fg=user.color)
		self.field.delete(0, END)
		self.field.insert(0, user.name.get())
