__author__ = 'miko'
from de.hochschuletrier.jpy.candidates.Candidate import Candidate, SerializableCandidate
from de.hochschuletrier.jpy.jason.JSONBackupHandler import JSONBackupHandler
from de.hochschuletrier.jpy.Constants import Constants


class CandidateManager:
	def __init__(self, master):
		self.candidates = []
		self.maxCount = 4
		self.master = master
		usebackup = self.master.backupManager.usebackup

		if usebackup:
			backupHandle = JSONBackupHandler("candidates_backup.json")
			self.restoreCandidates(backupHandle.load())
		else:
			self.registerCandidates()

	def registerCandidates(self):
		colors = Constants.COLORS
		for candidate in range(0, self.maxCount):
			self.candidates.append(Candidate(candidate, colors[candidate]))

	def restoreCandidates(self, data):
		for candidate in data:
			self.candidates.append(Candidate(candidate["id"], candidate["name"], candidate["points"]))

	def getSerializableData(self):
		output = []
		for candidate in self.candidates:
			output.append(SerializableCandidate(candidate.id, candidate.name.get(), candidate.points.get()))
		return output
