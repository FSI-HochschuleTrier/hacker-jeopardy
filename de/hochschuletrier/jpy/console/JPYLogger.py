__author__ = 'miko'


class JPYLogger:
	def __init__(self, caller):
		self.caller = caller.__class__.__name__
		self.color = self.getColor()

	def log(self, message):
		print(self.__class__.__name__ + "[LOG] >> " + self.caller + "\t--  " + message)

	def prompt(self, message):
		print(self.color + self.__class__.__name__ + "[GAMEINFO] >> " + self.caller + "\t--  " + message + "\033[0m")

	def getColor(self):
		if self.caller == "BackupManager":
			return "\033[0;;34m"
		elif self.caller == "JPYButton":
			return "\033[0;;35m"
		else:
			return ""
