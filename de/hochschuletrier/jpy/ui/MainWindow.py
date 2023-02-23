__author__ = 'miko'

import pyglet
import threading

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

	# pumping `pyglets`'s mainloop
	def pump(self):
		threading.Timer(0.1, self.pump).start()
		pyglet.clock.tick()
		pyglet.app.platform_event_loop.dispatch_posted_events()
	

	def mainloop(self):
		self.pump()
		super().mainloop()