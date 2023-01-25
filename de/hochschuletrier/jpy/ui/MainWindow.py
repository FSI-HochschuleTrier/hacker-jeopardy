__author__ = 'miko'
from tkinter import Tk
from de.hochschuletrier.jpy.Constants import Constants, Fonts


class MainWindow(Tk):
	def __init__(self, master, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs)
		self.attributes("-fullscreen", True)
		self.config(background="black", cursor="none")
		self.title("Jeopardy")
		Constants.SCREENW = self.winfo_screenwidth()
		Constants.SCREENH = self.winfo_screenheight()
		Fonts.construct()
