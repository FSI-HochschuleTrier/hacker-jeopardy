__author__ = 'miko'
from Tkinter import StringVar, IntVar


class Candidate:
    def __init__(self, id, name=""):
        self.name = StringVar()
        self.points = IntVar()
        self.id = id
        self.name.set("Player " + str(self.id + 1))

    def addPoints(self, points):
        oldPoints = self.points.get()
        oldPoints += points
        self.points.set(oldPoints)

    def subPoints(self, points):
        oldPoints = self.points.get()
        oldPoints -= points
        self.points.set(oldPoints)