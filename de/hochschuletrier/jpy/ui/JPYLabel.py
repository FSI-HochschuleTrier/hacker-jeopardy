from Tkinter import *
from de.hochschuletrier.jpy.Constants import Constants, Fonts


class JPYLabel(Frame):
	def __init__(self, *args, **kwargs):
		Frame.__init__(self, *args)
		self.label = ""
		self.text = kwargs["text"]
		self.font = Fonts.SYSTEM_REGULAR
		self.config(
			width=Constants.SCREENW / 6 + 1,
			height=Constants.SCREENH / 7,
			background="#FFCC00"
		)
		self.pack_propagate(0)
		self.innerLabel()

	def innerLabel(self):
		self.label = Label(self, text=self.text)
		self.label.config(
			background="blue",
			foreground="white",
			bd=5,
			relief="solid",
			font=self.font,
			wraplength=Constants.SCREENW / 6
		)
		self.label.pack(fill=BOTH, expand=1)
