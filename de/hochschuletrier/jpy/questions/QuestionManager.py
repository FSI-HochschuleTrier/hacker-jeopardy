__author__ = 'miko'
from de.hochschuletrier.jpy.jason.JSONHandler import JSONHandler
from de.hochschuletrier.jpy.jason.JSONBackupHandler import JSONBackupHandler


class QuestionManager:
    def __init__(self, master, questiondir):
        self.master = master
        self.questiondir = questiondir
        self.questions = {}
        self.double = []
        self.questionSet = []
        self.categories = []
        self.candidate = None
        self.worth = 0
        self.usebackup = self.master.backupManager.usebackup

        self.requestData()
        if self.usebackup:
            backupHandle = JSONBackupHandler("questions_backup.json")
            self.restoreQuestionSet(backupHandle.load())
        else:
            self.initQuestionSet()

    def requestData(self):
        jsonHandle = JSONHandler("questions/" + self.questiondir + "/questions.json")
        self.double = jsonHandle.double
        self.categories = jsonHandle.getCategories()
        for cat in self.categories:
            self.questions[cat.name] = cat.questions

    def restoreQuestionSet(self, data):
        self.questionSet = data
        print self.questionSet

    def initQuestionSet(self):
        for questionset in self.questions:
            q = []
            for question in self.questions[questionset]:
                q.append(1)
            self.questionSet.append(q)