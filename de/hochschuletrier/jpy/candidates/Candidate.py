__author__ = 'miko'
from Tkinter import StringVar, IntVar


class Candidate(object):
    def __init__(self, id, name="", points=0):
        self.name = StringVar()
        self.points = IntVar()
        self.id = id
        if points != 0:
            self.points.set(points)
        if name == "":
            self.name.set("Player " + str(self.id + 1))
        else:
            self.name.set(name)

    def addPoints(self, points):
        oldPoints = self.points.get()
        oldPoints += points
        self.points.set(oldPoints)

    def subPoints(self, points):
        oldPoints = self.points.get()
        oldPoints -= points
        self.points.set(oldPoints)


class SerializableCandidate:
    def __init__(self, id, name, points):
        self.id = int(id)
        self.name = str(name)
        self.points = int(points)

    def default(obj):
        if isinstance(obj, SerializableCandidate):
            return obj.__dict__
        return obj