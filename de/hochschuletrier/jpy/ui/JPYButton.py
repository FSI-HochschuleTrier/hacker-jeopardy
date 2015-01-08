__author__ = 'miko'

from Tkinter import *
from tkFont import Font
from de.hochschuletrier.jpy.Constants import Constants, Fonts


class JPYButton(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args)
        self.text = kwargs['text']
        self.button = ""
        self.questionText = kwargs['question']
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
        self.master.root.questionManager.worth = self.worth
        self.button["font"] = self.font2
        self.button["foreground"] = "#FFCC00"
        self.button["text"] = event.widget.master.questionText
        self.master.overlayManager.overlays[0].text.set(event.widget.master.questionText)
        self.master.root.questionManager.questionSet[self.questionID[0]][self.questionID[1]] = 0
        self.master.after(1300, self.processOverlay)
        self.master.root.audioManager.playBackgroundSong()

    def processOverlay(self):
        self.button["text"] = ""
        self.master.overlayManager.showOverlay(0)
