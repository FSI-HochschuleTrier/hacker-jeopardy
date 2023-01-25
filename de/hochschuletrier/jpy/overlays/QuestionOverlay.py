__author__ = 'miko'
from de.hochschuletrier.jpy.overlays.Overlay import Overlay
from de.hochschuletrier.jpy.Constants import Constants, Fonts
from tkinter import Label
from PIL import Image, ImageTk


class QuestionOverlay(Overlay):
	def __init__(self, *args, **kwargs):
		Overlay.__init__(self, *args, **kwargs)
		self.label = ""
		self.config(background="blue")
		self.audio = ""
		self.lastButton = ""
		self.drawLabel()

	def drawLabel(self):
		self.label = Label(self)
		self.label.config(
			textvar=self.text,
			font=Fonts.SYSTEM_BIG,
			background=self["background"],
			foreground="white",
			wraplength=Constants.SCREENW * 0.8
		)

		self.label.place(relwidth=1, relheight=1)

	def highlight(self, color):
		self.config(background=color)
		self.label.config(background=color)
		return

	def normalize(self):
		self.config(background="blue")
		self.label.config(background="blue")
		return

	def hide(self, event):
		Overlay.hide(self, event)
		self.normalize()

	def setimage(self, url):
		# Todo: url
		# url = 'resources/20140312_153545.jpg'
		# url = 'resources/boot.jpg'
		img = Image.open(url)
		self.img = img.resize((1280, 720))
		self.image = ImageTk.PhotoImage(self.img)
		self.label.config(image=self.image)

	def setAudio(self, url):
		self.audio = url

	def playAudio(self):
		self.root.root.audioManager.playQuestion(self.audio)

	def stopAudio(self):
		self.root.root.audioManager.stopQuestion()
		self.audio = ""

	def delimage(self):
		self.drawLabel()
