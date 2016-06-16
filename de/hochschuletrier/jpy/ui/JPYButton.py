__author__ = 'miko'

from Tkinter import *
from tkFont import Font
from de.hochschuletrier.jpy.Constants import Constants, Fonts
from de.hochschuletrier.jpy.console.JPYLogger import JPYLogger
import time


class JPYButton(Frame):
	def __init__(self, *args, **kwargs):
		Frame.__init__(self, *args)
		self.root = kwargs['root']
		self.logger = JPYLogger(self)
		self.text = kwargs['text']
		self.button = ""
		self.qCategory = kwargs['qCategory']
		self.double = kwargs["double"]
		self.questionText = kwargs['question']
		self.category = kwargs['category']
		self.worth = int(kwargs['worth'])
		self.font = Fonts.MONEY_BIG
		self.font2 = Fonts.MONEY_SMALL
		self.questionID = kwargs['questionID']
		self.pack_propagate(0)
		self.config(
			background="#FFCC00",
			width=Constants.SCREENW / 6 + 1,
			height=Constants.SCREENH / 7 + 1
		)
		self.innerButton()

	def innerButton(self):
		self.button = Button(self, text=self.text, font=self.font)
		self.button.config(
			background="blue",
			activebackground="blue",
			foreground="white",
			activeforeground="#FFCC00",
			highlightbackground="black",
			relief="solid",
			wraplength=Constants.SCREENW / 6 - 10,
			bd=4
		)
		self.button.bind("<Button-1>", self.activateQuestion)
		self.button.pack(fill=BOTH, expand=1)

	def activateQuestion(self, event):
		if not self.master.root.gameStarted:
			return
		if self.double:
			self.doubleJeopardy(event)
		else:
			self.root.gameStateManager.states[1].overlayManager.overlays[2].hide(self)
		if self.button["text"] == "":
			return
		if self.root.gameStateManager.states[1].overlayManager.overlays[2].isVisible:
			return
		self.master.root.questionManager.worth = self.worth
		self.button["font"] = self.font2
		self.button["foreground"] = "#FFCC00"
		questionText = event.widget.master.questionText
		self.button["text"] = questionText
		self.master.overlayManager.overlays[0].text.set(event.widget.master.questionText)

		self.logger.prompt("Frage: " + self.root.questionManager.answers[self.qCategory.name][self.questionID[1]])
		if event.widget.master.category == "image":
			self.button["text"] = "Bild"
			directory = self.master.root.questionManager.questiondir
			self.master.overlayManager.overlays[0].setimage("questions/" + directory + "/" + questionText)
		elif event.widget.master.category == "audio":
			self.master.overlayManager.overlays[0].delimage()
			self.button["text"] = "Audio"
			self.master.overlayManager.overlays[0].text.set("Audio")
			directory = self.master.root.questionManager.questiondir
			self.master.overlayManager.overlays[0].setAudio("questions/" + directory + "/" + questionText)
			time.sleep(1)
			self.master.overlayManager.overlays[0].playAudio()
		else:
			self.master.overlayManager.overlays[0].delimage()
		self.master.root.questionManager.questionSet[self.questionID[0]][self.questionID[1]] = 0
		self.master.after(1300, self.processOverlay)
		if not self.master.root.audioManager.playingBackground() and event.widget.master.category != "audio":
			self.master.root.audioManager.playBackgroundSong()

	def processOverlay(self):
		self.button["text"] = ""
		self.master.overlayManager.showOverlay(0)
		if self.double:
			self.master.overlayManager.root.double.worth.set(2 * self.worth)
			self.master.overlayManager.root.double.lift()
			self.master.root.questionManager.toggledouble = True

	def doubleJeopardy(self, event):
		self.root.gameStateManager.states[1].overlayManager.overlays[2].setCaller(self, event)
		self.root.gameStateManager.states[1].overlayManager.showOverlay(2)
		self.double = False
