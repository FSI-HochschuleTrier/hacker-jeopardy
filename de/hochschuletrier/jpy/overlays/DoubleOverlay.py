__author__ = 'georg'

from de.hochschuletrier.jpy.Constants import Constants, Fonts
from de.hochschuletrier.jpy.overlays.Overlay import Overlay
from Tkinter import Label, StringVar

class DoubleOverlay(Overlay):
    def __init__(self, *args, **kwargs):
        Overlay.__init__(self, *args, **kwargs)
        self.label = ""
        self.money = ""
        self.worth = StringVar()
        self.config(
            padx=0,
            pady=30,
            bd=4,
            background="gold"
        )
        self.place(x=0, y=0, relwidth=1, relheight=1, width=-1400, height=-750)

        self.renderLabel()

    def renderLabel(self):
        self.label = Label(self)
        self.label.config(
            text="Double Jeopardy",
            font=Fonts.MONEY_MEDIUM,
            background="gold"
        )
        self.label.pack()

        self.money = Label(self)
        self.money.config(
            textvar=self.worth,
            font=Fonts.MONEY_BIG,
            background="gold",
            wraplength=Constants.SCREENW
        )
        self.money.pack()