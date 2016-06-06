__author__ = 'miko'
from de.hochschuletrier.jpy.jason.JSONBackupHandler import JSONBackupHandler
from de.hochschuletrier.jpy.console.JPYLogger import JPYLogger

class BackupManager:
    def __init__(self, root):
        self.root = root
        self.usebackup = False
        self.dobackup = True
        self.logger = JPYLogger(self)
        self.fileName_candidates = "candidates_backup.json"
        self.fileName_questions = "questions_backup.json"
        self.jsonCandidatesHandler = JSONBackupHandler(self.fileName_candidates)
        self.jsonQuestionsHandler = JSONBackupHandler(self.fileName_questions)
        if self.dobackup:
            self.root.mainWindow.after(1000, self.performBackup)

    def performBackup(self):
        self.backupCandidates()
        self.backupQuestions()
        self.root.mainWindow.after(5000, self.performBackup)
        #self.logger.prompt("NOTICE :: Gamesession have been saved to file.")

    def backupQuestions(self):
        self.jsonQuestionsHandler.save(self.root.questionManager.questionSet)

    def backupCandidates(self):
        self.jsonCandidatesHandler.save(self.root.candidateManager.getSerializableData())

