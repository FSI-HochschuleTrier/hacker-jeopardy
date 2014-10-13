__author__ = 'miko'
from de.hochschuletrier.jpy.jason.JSONBackupHandler import JSONBackupHandler
from de.hochschuletrier.jpy.console.JPYLogger import JPYLogger

class BackupManager:
    def __init__(self, root):
        self.root = root
        self.logger = JPYLogger(self)
        self.fileName = "backup.json"
        self.jsonHandler = JSONBackupHandler(self.fileName)
        self.root.mainWindow.after(1000, self.backupCandidates)


    def backupCandidates(self):
        self.jsonHandler.save(self.root.candidateManager.getSerializableDate())
        self.logger.prompt("NOTICE :: Candidates have been saved to file.")
        self.root.mainWindow.after(5000, self.backupCandidates)

