__author__ = 'miko'
from tkinter import Frame, StringVar


class Overlay(Frame):
	def __init__(self, *args, **kwargs):
		self.overlayName = kwargs["overlayName"]
		self.root = args[0]
		self.id = kwargs["id"]
		self.text = StringVar()
		self.image = None
		self.isVisible = False
		Frame.__init__(self, self.root)
		self.config(
			padx=50,
			pady=50,
			relief="solid",
			bd=35,
			highlightbackground="black"
		)
		self.place(x=60, y=60, relwidth=1, relheight=1, width=-120, height=-120)

	def hide(self, event):
		self.lower()
		self.isVisible = False
