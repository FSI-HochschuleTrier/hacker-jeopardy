__author__ = 'miko'
from de.hochschuletrier.jpy.candidates.Candidate import Candidate


class CandidateManager:
    def __init__(self, master):
        self.candidates = []
        self.maxCount = 4
        self.master = master

        self.registerCandidates()

    def registerCandidates(self):
        for candidate in range(0, self.maxCount):
            self.candidates.append(Candidate(candidate))