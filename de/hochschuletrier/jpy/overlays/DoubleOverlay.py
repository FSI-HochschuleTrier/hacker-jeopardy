__author__ = 'georg'

from de.hochschuletrier.jpy.input.InputController import InputController
from de.hochschuletrier.jpy.Constants import Fonts, Constants
from de.hochschuletrier.jpy.overlays.Overlay import Overlay
from de.hochschuletrier.jpy.console.JPYLogger import JPYLogger
from tkinter import Label, Entry, Button, END


class DoubleOverlay(Overlay):
	def __init__(self, *args, **kwargs):
		Overlay.__init__(self, *args, **kwargs)
		self.label = ""
		self.field = ""
		self.button = ""
		self.logger = JPYLogger(self)
		self.bLabel = ""
		self.config(
			background="gold",
			cursor="arrow",
			bd=35
		)
		self.place(x=Constants.SCREENW / 4, y=(Constants.SCREENH/10)*2, relwidth=0.5, relheight=0.6, width=10, height=10)
		self.caller = ""
		self.selectedCandidate = 0
		self.settedPoints = 0

		self.renderLabel()
		self.renderField()
		self.renderButton()


	def renderLabel(self):
		self.label = Label(self)
		self.label.config(
			text="DOUBLE JEOPARDY",
			font=Fonts.MONEY_BIG,
			background="gold"
		)
		self.label.pack()

	def renderField(self):
		self.field = Entry(self)
		self.field.config(
			relief="solid",
			bd=2,
			width=5,
			highlightcolor="black",
			font=Fonts.USER_LABEL_NAME_BIG
		)
		self.field.pack()

	def renderButton(self):
		self.bLabel = Label(self, text='\n', background="gold", width=0)
		self.bLabel.pack()
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
		try:
			self.settedPoints = int(self.field.get())
		except ValueError:
			return
		if self.settedPoints < self.caller.worth or self.settedPoints > 2 * self.caller.worth:
			return
		if self.root.root.questionManager.candidate is None:
			return

		self.logger.prompt("DOUBLE JEOPARDY!!!")
		self.logger.prompt("candidate " + str(self.selectedCandidate) + " has set " + str(self.settedPoints) + " points")
		self.root.root.questionManager.candidate = self.root.root.candidateManager.candidates[self.selectedCandidate]
		self.root.root.gameStateManager.states[1].overlayManager.overlays[0].highlight(
			self.root.root.questionManager.candidate.color)
		self.hide(self)
		self.caller.activateQuestion(self.oldEvent)

	def nextCandidate(self, event):
		if self.isVisible:
			numCandidates = len(self.master.root.candidateManager.candidates)
			if (self.selectedCandidate + 1 < numCandidates):
				self.selectedCandidate += 1
			else:
				self.selectedCandidate = 0
			self.root.root.questionManager.candidate = self.root.root.candidateManager.candidates[self.selectedCandidate]
			self.highlight(self.root.root.questionManager.candidate.color)


	def prevCandidate(self, event):
		numCandidates = len(self.master.root.candidateManager.candidates)
		if self.isVisible:
			if (self.selectedCandidate - 1 >= 0):
				self.selectedCandidate -= 1
			else:
				self.selectedCandidate = numCandidates - 1
			self.root.root.questionManager.candidate = self.root.root.candidateManager.candidates[self.selectedCandidate]
			self.highlight(self.root.root.questionManager.candidate.color)

	def highlight(self, color):
		self.config(background=color)
		self.label.config(background=color)
		self.bLabel.config(background=color)
		self.button.config(foreground=color)
		return

	def setCaller(self, caller, event):
		self.caller = caller
		self.oldEvent = event

	def clear(self):
		self.field.delete(0, END)
