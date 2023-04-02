__author__ = 'miko'
from de.hochschuletrier.jpy.ui.JPYLabel import JPYLabel
from de.hochschuletrier.jpy.ui.JPYUserLabel import JPYUserLabel
from de.hochschuletrier.jpy.ui.JPYButton import JPYButton
from math import ceil
from de.hochschuletrier.jpy.jason.JSONHandler import JSONHandler
from tkinter import LEFT, BOTH, Frame, EW

class UserBar(Frame):
	def __init__(self, parent, root):
		super().__init__(parent, bg="green")
		self.root = root

class TableProcessor:
	cols = 6
	rows = 7

	def __init__(self, parent, root):
		self.root = root
		self.parent = parent
		self.buildTableHead()
		self.buildTableBody()
		self.buildCandidates()

	def buildTableHead(self):
		for header in range(6):
			JPYLabel(self.parent, text=self.root.questionManager.categories[header].name).grid(row=0, column=header)

	def buildTableBody(self):
		for row in range(1, 6):
			for col in range(6):
				values = [100, 200, 300, 400, 500, 600]
				count = (row - 1) * 6 + col
				if self.root.questionManager.questionSet[col][row - 1] == 1:
					text = "$" + str(values[row - 1])
				# text = str((row - 1) * 6 + col)
				else:
					text = ""
				JPYButton(
					self.parent,
					root=self.root,
					question=self.root.questionManager.questions[self.root.questionManager.categories[col].name][row - 1],
					text=text,
					qCategory=self.root.questionManager.categories[col],
					double=(True if count in self.root.questionManager.double else False),
					worth=values[row - 1],
					questionID=[col, row - 1],
					borderwidth=1,
					category=self.root.questionManager.categories[col].type,
				).grid(row=row, column=col)

	def buildCandidates(self):
		max = len(self.root.candidateManager.candidates)
		userBar = UserBar(self.parent, self.root)

		for candidate in self.root.candidateManager.candidates:
			cLabel = JPYUserLabel(parent = userBar, back=candidate.color, user=candidate, numPlayers = max)
			cLabel.pack(side=LEFT, expand=True, fill=BOTH)

		userBar.grid(row=6, column=0, columnspan=6, sticky=EW)
