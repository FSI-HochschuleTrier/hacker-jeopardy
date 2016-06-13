__author__ = 'georg'

from de.hochschuletrier.jpy.input.InputController import InputController
from de.hochschuletrier.jpy.Constants import Fonts
from de.hochschuletrier.jpy.overlays.Overlay import Overlay
from de.hochschuletrier.jpy.console.JPYLogger import JPYLogger
from Tkinter import Label, Entry, Button, END


class DoubleOverlay(Overlay):
	def __init__(self, *args, **kwargs):
		Overlay.__init__(self, *args, **kwargs)
		self.label = ""
		self.field = ""
		self.button = ""
		self.user = ""
		self.logger = JPYLogger(self)
		self.config(
			background="red",
			cursor="arrow"
		)
		self.caller = ""

		self.renderLabel()
		self.renderField()
		self.renderButton()

	def renderLabel(self):
		self.label = Label(self)
		self.label.config(
			text="DOUBLE JEOPARDY",
			font=Fonts.MONEY_BIG,
			background="red"
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
		self.field.pack()

	def renderButton(self):
		Label(self, text='\n', background="red").pack()
		self.button = Button(self)
		self.button.config(
			text="OK",
			relief="solid",
			background="black",
			foreground="red",
			font=Fonts.MONEY_MEDIUM,
			command=self.save
		)
		self.button.pack()

	def save(self, event=""):
		self.logger.prompt("DOUBLE JEOPARDY!!!")
		self.hide(self)
		InputController.blockBuzzer = False

	def insert(self, user):
		self.field.delete(0, END)
		self.field.insert(0, user.name.get())

	def setCaller(self, caller, event):
		self.caller = caller
		self.oldEvent = event
		self.button.bind("<Button-1>", self.callback)

	def callback(self, event):
		self.caller.activateQuestion(self.oldEvent)
