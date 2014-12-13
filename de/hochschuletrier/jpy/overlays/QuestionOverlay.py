__author__ = 'miko'
from de.hochschuletrier.jpy.overlays.Overlay import Overlay
from de.hochschuletrier.jpy.Constants import Constants, Fonts
from Tkinter import Label


class QuestionOverlay(Overlay):
    def __init__(self, *args, **kwargs):
        Overlay.__init__(self, *args, **kwargs)
        self.label = ""
        self.config(background="blue")

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

    def normalize(self):
        self.config(background="blue")
        self.label.config(background="blue")

    def hide(self, event):
        Overlay.hide(self, event)
        self.normalize()