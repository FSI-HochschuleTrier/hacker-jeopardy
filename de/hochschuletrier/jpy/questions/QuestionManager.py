__author__ = 'miko'
from de.hochschuletrier.jpy.jason.JSONHandler import JSONHandler


class QuestionManager:
    def __init__(self, questionset):
        self.questionset = questionset
        self.questions = {}
        self.categories = []
        self.candidate = None
        self.worth = 0

        self.requestData()

    def requestData(self):
        jsonHandle = JSONHandler(self.questionset)
        self.questions = jsonHandle.getQuestions()
        self.categories = jsonHandle.getCategories()