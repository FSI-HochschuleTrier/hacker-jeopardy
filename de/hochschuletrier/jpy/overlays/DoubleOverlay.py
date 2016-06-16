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
		self.logger = JPYLogger(self)
		self.config(
			background="red",
			cursor="arrow"
		)
		self.caller = ""
		self.selectedCandidate = 0
		self.settedPoints = 0

		self.renderLabel()
		self.renderField()
		self.renderButton()

		self.root.root.questionManager.candidate = self.root.root.candidateManager.candidates[self.selectedCandidate]
		self.highlight(self.root.root.questionManager.candidate.color)


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

		self.logger.prompt("DOUBLE JEOPARDY!!!")
		self.logger.prompt("candidate " + str(self.selectedCandidate) + " has set " + str(self.settedPoints) + " points")
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
		return

	def setCaller(self, caller, event):
		self.caller = caller
		self.oldEvent = event

	def clear(self):
		self.field.delete(0, END)
